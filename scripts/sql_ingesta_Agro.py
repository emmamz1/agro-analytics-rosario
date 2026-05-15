import pandas as pd
from sqlalchemy import create_engine
import urllib

# 1. Conexión
server_name = r'DESKTOP-5JJVFNC\SQLEXPRESS' 
params = urllib.parse.quote_plus(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={r'.\SQLEXPRESS'};'
    f'DATABASE=AgroIndustria_Rosario;'
    f'Trusted_Connection=yes;'
)
engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# 2. Carga del archivo
df = pd.read_csv(r'agro-logistica\estimaciones_rosario_final.csv')

# 3. RENOMBRADO (Mapeo)
df = df.rename(columns={
    'campania': 'campaña',
    'provincia': 'provincia_nombre',
    'departamento': 'departamento_nombre',
    'cultivo': 'cultivo_nombre',
    'superficie_sembrada_ha': 'superficie_sembrada_hectareas',
    'superficie_cosechada_ha': 'superficie_cosechada_hectareas',
    'produccion_tm': 'produccion_toneladas',
    'rendimiento_kgxha': 'rendimiento_kg_x_hectarea'
})

# 2. SELECCIÓN (Paso crítico para solucionar el error)
# Creamos una lista con los nombres exactos de las columnas de tu tabla SQL
columnas_validas = [
    'campaña', 
    'provincia_nombre', 
    'departamento_nombre', 
    'cultivo_nombre',
    'superficie_sembrada_hectareas', 
    'superficie_cosechada_hectareas', 
    'produccion_toneladas', 
    'rendimiento_kg_x_hectarea'
]

# Filtramos el DataFrame: esto elimina 'anio', 'provincia_id', etc.
df_final = df[columnas_validas]

# 3. CARGA FINAL
# Usamos df_final para que no haya columnas extrañas
df_final.to_sql('EstimacionesAgro', con=engine, if_exists='append', index=False)