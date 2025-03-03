import pandas as pd

# Cargar el archivo CSV de Tokyo (asegúrate de que el archivo está en el mismo directorio que este script)
file_name = "Tokyo, Japon.csv"
df_tokyo = pd.read_csv(file_name)

# Función para reemplazar valores nulos con la mediana en columnas numéricas
def reemplazar_nulos_mediana(df):
    df_numeric = df.select_dtypes(include=['int64', 'float64'])
    df[df_numeric.columns] = df_numeric.fillna(df_numeric.median())
    df.to_csv("salida_mediana.csv", index=False)
    return df

# Función para reemplazar valores nulos con 'ffill' en columnas tipo object, datetime y category
def reemplazar_nulos_ffill(df):
    df_categoric = df.select_dtypes(include=['object', 'datetime', 'category'])
    df[df_categoric.columns] = df_categoric.fillna(method='ffill')
    df.to_csv("salida_ffill.csv", index=False)
    return df

# Función para reemplazar valores nulos con 'bfill' en columnas tipo object, datetime y category
def reemplazar_nulos_bfill(df):
    df_categoric = df.select_dtypes(include=['object', 'datetime', 'category'])
    df[df_categoric.columns] = df_categoric.fillna(method='bfill')
    df.to_csv("salida_bfill.csv", index=False)
    return df

# Función para reemplazar valores nulos con un string específico en columnas tipo object, datetime y category
def reemplazar_nulos_string(df, string_value="Sin datos"):
    df_categoric = df.select_dtypes(include=['object', 'datetime', 'category'])
    df[df_categoric.columns] = df_categoric.fillna(string_value)
    df.to_csv("salida_string.csv", index=False)
    return df

# Función para reemplazar valores nulos con una constante en columnas numéricas
def reemplazar_nulos_constante(df, constante=0):
    df_numeric = df.select_dtypes(include=['int64', 'float64'])
    df[df_numeric.columns] = df_numeric.fillna(constante)
    df.to_csv("salida_constante.csv", index=False)
    return df

# Aplicar funciones al dataset de Tokyo
df_mediana = reemplazar_nulos_mediana(df_tokyo.copy())
df_ffill = reemplazar_nulos_ffill(df_tokyo.copy())
df_bfill = reemplazar_nulos_bfill(df_tokyo.copy())
df_string = reemplazar_nulos_string(df_tokyo.copy(), "Sin datos")
df_constante = reemplazar_nulos_constante(df_tokyo.copy(), -1)

print("Archivos generados exitosamente en el directorio actual:")
print("- salida_mediana.csv")
print("- salida_ffill.csv")
print("- salida_bfill.csv")
print("- salida_string.csv")
print("- salida_constante.csv")