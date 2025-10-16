from sqlalchemy import or_
from sqlalchemy.orm import Session
from schemas import s_receta
from models import Receta, Ingrediente, Usuario
from typing import Union, Optional
from fastapi import status, APIRouter, HTTPException, Query
from config.database import Session

router = APIRouter()

@router.get("/", status_code= status.HTTP_200_OK, response_model= list[s_receta.RecetaGetSchema])
def get_recetas(ingredientes: Optional[str] = Query(None, description="Filtro por nombre de ingrediente")):
    db = Session()
    if ingredientes:
        ingredientes_separados = [t.strip().lower() for t in ingredientes.split(",") if t.strip()]
        result = (
            db.query(Receta)
            .join(Ingrediente)
            .filter(or_(*[Ingrediente.nombre.ilike(f"%{i}%") for i in ingredientes_separados]))
            .distinct()
            .all()
        )
    else:
        result = db.query(Receta).all()

    if not result:
        raise HTTPException(status_code=404, detail="No se ha encontrado ninguna receta")
    return result 

@router.get("/{receta_id}",status_code= status.HTTP_200_OK, response_model= s_receta.RecetaCreateSchema)
def get_receta(receta_id: int):
    db = Session()
    result = db.query(Receta).filter(Receta.id == receta_id).first()
    return result   

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=s_receta.RecetaCreateSchema)
def crear_receta(receta: s_receta.RecetaCreateSchema):
    db = Session()
    if not receta.ingredientes:
        raise HTTPException(status_code=400, detail= "Debe incluir al menos un ingrediente")
    if not receta.nombre:
        raise HTTPException(status_code=400, detail= "Debe incluir el título de la receta")
    if not receta.preparacion:
        raise HTTPException(status_code=400, detail= "Debe incluir la preparación de la receta")
    if not receta.tiempo_preparacion:
        raise HTTPException(status_code=400, detail= "Debe incluir el tiempo de preparación de la receta")
    
    nueva_receta = Receta(
        nombre=receta.nombre,
        preparacion=receta.preparacion,
        tiempo_preparacion=receta.tiempo_preparacion,
        imagen_url=receta.imagen_url,
        video_url=receta.video_url
    )
    for ingrediente in receta.ingredientes:
        nueva_receta.ingredientes.append(
            Ingrediente(
                nombre=ingrediente.nombre,
                cantidad=ingrediente.cantidad,
                unidad=ingrediente.unidad
            )
        )    
    db.add(nueva_receta)
    db.commit()
    db.refresh(nueva_receta) 
    
    return nueva_receta  