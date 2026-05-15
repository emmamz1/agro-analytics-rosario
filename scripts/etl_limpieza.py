import pandas as pd
import unicodedata

def normalizar_texto(texto):
    if not isinstance(texto, str): return texto
    # Decodificar posibles errores de encoding
    try:
        texto = texto.encode('latin1').decode('utf-8')
    except:
        pass
    
    # Quitar acentos y normalizar
    texto = "".join(
        c for c in unicodedata.normalize('NFKD', texto)
        if not unicodedata.combining(c)
    )
    return texto.strip().upper()


ruta_local = r"C:\Users\emmam\Documents\Proyectos emma\datasets emma\estimaciones-agricolas-2026-03.csv"


# Pruebo leerlo
try:
    df = pd.read_csv(ruta_local, encoding='utf-8')
except:
    df = pd.read_csv(ruta_local, encoding='latin1')

# Aplico la limpieza a las columnas de búsqueda
df['dept_clean'] = df['departamento'].apply(normalizar_texto)
df['cult_clean'] = df['cultivo'].apply(normalizar_texto)


depts = ['ROSARIO', 'SAN LORENZO', 'VILLA CONSTITUCION', 'CONSTITUCION', 'CASEROS']
cultivos = ['SOJA TOTAL', 'MAIZ', 'TRIGO TOTAL']

# Filtro isin para no traer registros incorrectos
df_rosario = df[
    (df['dept_clean'].isin(depts)) & 
    (df['cult_clean'].isin(cultivos))
].copy()

# Limpio las columnas temporales antes de guardar
df_rosario.drop(columns=['dept_clean', 'cult_clean'], inplace=True)

print(f"Éxito: Se encontraron {len(df_rosario)} filas.")
print(f"Cultivos detectados: {df_rosario['cultivo'].unique()}")
print(f"Departamentos detectados: {df_rosario['departamento'].unique()}")

# Guardo para SQL
df_rosario.to_csv('estimaciones_rosario_final.csv', index=False, encoding='utf-8-sig')

