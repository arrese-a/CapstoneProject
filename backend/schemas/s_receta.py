from pydantic import BaseModel
from typing import List, Optional

class IngredienteSchema(BaseModel):
    nombre: str
    cantidad: float
    unidad: str

class RecetaCreateSchema(BaseModel):
    nombre: str
    preparacion: str
    tiempo_preparacion: str
    imagen_url: Optional[str] = None
    video_url: Optional[str] = None
    ingredientes: List[IngredienteSchema]

class RecetaGetSchema(BaseModel):
    id: int
    nombre: str
    preparacion: str
    tiempo_preparacion: str
    imagen_url: Optional[str] = None
    video_url: Optional[str] = None
    ingredientes: List[IngredienteSchema]

    class Config:
        orm_mode = True
