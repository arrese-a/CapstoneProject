# from sqlalchemy.orm import Session
from models import Receta, ListaCompra
from fastapi import status, APIRouter
from fastapi.responses import JSONResponse
from config.database import Session
router = APIRouter()

@router.post("/agregar", status_code=status.HTTP_200_OK)
def agregar_ingredientes_lista(usuario_id: int, receta_id: int):
    db = Session()
    receta = db.query(Receta).filter(Receta.id == receta_id).first()
    if not receta:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Receta no encontrada"})
    for ingrediente in receta.ingredientes:
        existente = db.query(ListaCompra).filter_by(
            usuario_id=usuario_id,
            ingrediente_nombre=ingrediente.nombre,
            unidad=ingrediente.unidad
        ).first()

        if existente:
            existente.cantidad += ingrediente.cantidad
        else:
            nuevo_ingrediente = ListaCompra(
                usuario_id=usuario_id,
                ingrediente_nombre=ingrediente.nombre,
                cantidad=ingrediente.cantidad,
                unidad=ingrediente.unidad
            )
            db.add(nuevo_ingrediente)
    db.commit()
    return {"message": "Ingredientes agregados a la lista de compra"}

@router.get("/obtener/{usuario_id}")
def get_lista_compra(usuario_id: int):
    db = Session()
    ingredientes = db.query(ListaCompra).filter(ListaCompra.usuario_id == usuario_id).all()

    resultado = {}
    for ingrediente in ingredientes:
        completo = (ingrediente.ingrediente_nombre, ingrediente.unidad)
        if completo in resultado:
            resultado[completo] += ingrediente.cantidad
        else:
            resultado[completo] = ingrediente.cantidad
    
    lista_final = [
        {"nombre": nombre, "unidad": unidad, "cantidad": cantidad}
        for (nombre, unidad), cantidad in resultado.items()
    ]

    return JSONResponse(status_code=status.HTTP_200_OK, content=lista_final)
