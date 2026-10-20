import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

usuario = os.getenv("DB_USER")
contrasena = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
puerto = os.getenv("DB_PORT")
base = os.getenv("DB_NAME")

cadena = f"postgresql+psycopg2://{usuario}:{contrasena}@{host}:{puerto}/{base}"

try:
    engine = create_engine(cadena)
    with engine.connect() as conn:
        resultado = conn.execute(text("SELECT 1"))
        print("Conexión correcta:", resultado.scalar())
except Exception as e:
    print("Error de conexión:", e)