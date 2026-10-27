import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

def obtener_motor_bd():
    """Crea y devuelve el motor de conexión a PostgreSQL leyendo el .env"""
    load_dotenv()
    
    usuario = os.getenv("DB_USER")
    contrasena = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    puerto = os.getenv("DB_PORT")
    base = os.getenv("DB_NAME")
    
    cadena = f"postgresql+psycopg2://{usuario}:{contrasena}@{host}:{puerto}/{base}"
    return create_engine(cadena)

def cargar_a_postgres(df, nombre_tabla):
    """Carga un DataFrame en la tabla especificada de PostgreSQL"""
    
    # Control de seguridad: Evitar procesar DataFrames vacíos o nulos
    if df is None or df.empty:
        print("Error: No hay datos para cargar. El DataFrame está vacío.")
        return False
        
    try:
        print(f"Iniciando carga de {len(df)} registros en la tabla '{nombre_tabla}'...")
        engine = obtener_motor_bd()
        
        # El parámetro if_exists='append' añade los datos a los existentes. 
        # Si prefieres sobreescribir la tabla cada vez, usa if_exists='replace'
        df.to_sql(
            name=nombre_tabla, 
            con=engine, 
            if_exists='append', 
            index=False # Evita que el índice de Pandas se guarde como una columna extra
        )
        
        print("Carga completada con éxito.")
        return True
        
    except Exception as e:
        print(f"Error crítico durante la carga en Base de Datos: {e}")
        return False