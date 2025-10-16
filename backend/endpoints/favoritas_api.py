from sqlalchemy.orm import Session
from schemas import s_receta
from models import Receta, Ingrediente, Usuario
from typing import Union
from fastapi import status, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from config.database import Session

router = APIRouter()

@router.get("/{usuario_id}", status_code=status.HTTP_200_OK, response_model=list[s_receta.RecetaGetSchema])
def get_recetas_favoritas(usuario_id: int):
    db = Session()
    recetas_favoritas = db.query(Receta).join(Receta.usuarios_favoritos).filter_by(id=usuario_id).all()
    return recetas_favoritas

@router.post("/{usuario_id}/{receta_id}", status_code=status.HTTP_200_OK)
def agregar_receta_favorita(usuario_id: int, receta_id: int):
    db = Session()
    receta = db.query(Receta).filter(Receta.id == receta_id).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    if receta in usuario.recetas_favoritas:
        raise HTTPException(status_code=400, detail="La receta ya está en favoritos")
    
    usuario.recetas_favoritas.append(receta)
    db.commit()
    return {"message": "Receta agregada a favoritos"}

@router.delete("/{usuario_id}/{receta_id}", status_code=status.HTTP_200_OK)
def eliminar_receta_favorita(usuario_id: int, receta_id: int):
    db = Session()
    receta = db.query(Receta).filter(Receta.id == receta_id).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    if receta not in usuario.recetas_favoritas:
        raise HTTPException(status_code=400, detail="La receta no está en favoritos")
    
    usuario.recetas_favoritas.remove(receta)
    db.commit()
    return {"message": "Receta eliminada de favoritos"}

@router.get("/favorita-check/{usuario_id}/{receta_id}", status_code=status.HTTP_200_OK, response_model=Union[dict, bool])
def es_receta_favorita(usuario_id: int, receta_id: int):
    db = Session()
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    receta = db.query(Receta).filter(Receta.id == receta_id).first()
    if not receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"es_favorita": receta in usuario.recetas_favoritas}
    )