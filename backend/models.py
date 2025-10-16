from config.database import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.orm import relationship

favoritas = Table(
    'favoritas', 
    Base.metadata,
    Column('usuario_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('receta_id', Integer, ForeignKey('recetas.id'), primary_key=True)
)

class Usuario(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)  # Deberías encriptar la contraseña
    # session_id = Column(String, nullable=True)
    
    lista_compra = relationship("ListaCompra", back_populates="usuario")
    recetas_favoritas = relationship("Receta", secondary="favoritas", back_populates="usuarios_favoritos")


class Receta(Base):
    __tablename__ = "recetas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), index=True)
    preparacion = Column(String, index=True)
    tiempo_preparacion = Column(String, index=True)
    imagen_url = Column(String(255), index=True, nullable=True)
    video_url = Column(String(255), index=True, nullable=True)

    ingredientes = relationship("Ingrediente", back_populates="receta", cascade="all, delete-orphan")

    usuarios_favoritos = relationship("Usuario", secondary="favoritas", back_populates="recetas_favoritas")


class Ingrediente(Base):
    __tablename__ = "ingredientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    unidad = Column(String(50))  # Ej: "gr", "tazas", "ml"

    receta_id = Column(Integer, ForeignKey("recetas.id"), nullable=False)
    receta = relationship("Receta", back_populates="ingredientes")

class ListaCompra(Base):
    __tablename__ = "lista_compra"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    ingrediente_nombre = Column(String, nullable=False)
    cantidad = Column(Float, nullable=False)
    unidad = Column(String(50), nullable=False)

    usuario = relationship("Usuario", back_populates="lista_compra")