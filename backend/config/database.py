import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()
try:
    DATABASE_URL = os.environ.get("DATABASE_URL")
    print('Using DATABASE_URL:', DATABASE_URL)
except KeyError:
    print("Error: La variable de entorno 'DATABASE_URL' no está configurada.")
    API_KEY = "valor_por_defecto_o_fallo"

base_dir = os.path.dirname(os.path.realpath(__file__))

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

Base = declarative_base()