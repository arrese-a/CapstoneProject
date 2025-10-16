from fastapi import APIRouter, HTTPException, Request, Response, status
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
from config.database import Session
import secrets
from models import Usuario
from schemas import s_usuario # tu pydantic schema
from sqlalchemy.exc import IntegrityError

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SESSIONS = {}

@router.post("/signup")
def crear_usuario(usuario: s_usuario.UsuarioCreate, response: Response):
    db = Session()

    try:
        if not all([usuario.email, usuario.username, usuario.password]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Falta algún campo por rellenar. Por favor, completa todos los campos."
            )

        usuario.email = usuario.email.strip().lower()

        if db.query(Usuario).filter(Usuario.email == usuario.email).first():
            raise HTTPException(status_code=400, detail="El email ya existe")

        psw_encriptado = pwd_context.hash(usuario.password)

        nuevo_usuario = Usuario(
            username=usuario.username,
            email=usuario.email,
            password=psw_encriptado
        )
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="El email ya existe.")

    finally:
        db.close()

    session_id = secrets.token_hex(16)
    SESSIONS[session_id] = nuevo_usuario.id

    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        samesite="none",
        secure=True,
    )

    return {"message": "Registro exitoso", "usuario_id": nuevo_usuario.id}

@router.post("/login")
def login_usuario(usuario: s_usuario.UsuarioLogin, response: Response):
    db = Session()
    usuarioDb = db.query(Usuario).filter(Usuario.email == usuario.email).first()

    if not usuarioDb or not pwd_context.verify(usuario.password, usuarioDb.password):
        raise HTTPException(status_code=400, detail="Nombre de usuario o contraseña incorrectos.")

    session_id = secrets.token_hex(16)
    SESSIONS[session_id] = usuarioDb.id

    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True,
        samesite="none",
        secure=True,    
    )

    return {"message": "Login exitoso", "usuario_id": usuarioDb.id}

@router.get("/check-login")
def check_login(request: Request):
    session_id = request.cookies.get("session_id")
    if not session_id or session_id not in SESSIONS:
        return {"user": None}
    user_id = SESSIONS[session_id]
    return {"user": user_id}

@router.post("/logout")
def logout(response: Response, request: Request):
    session_id = request.cookies.get("session_id")
    if session_id and session_id in SESSIONS:
        del SESSIONS[session_id]
    response.delete_cookie(key="session_id")
    return {"message": "Logout exitoso"}