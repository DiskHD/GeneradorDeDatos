import pandas as pd
import numpy as np
import os

# Carga de archivos CSV con codificación especificada para evitar errores de decodificación
entidades_df = pd.read_csv(r'C:\Users\hdzdi\OneDrive\Documents\ITO\S6\ABD\CSV\ENTIDADES.csv', encoding='ISO-8859-1')
municipios_df = pd.read_csv(r'C:\Users\hdzdi\OneDrive\Documents\ITO\S6\ABD\CSV\MUNICIPIOS.csv', encoding='ISO-8859-1')
localidades_df = pd.read_csv(r'C:\Users\hdzdi\OneDrive\Documents\ITO\S6\ABD\CSV\LOCALIDADES.csv', encoding='ISO-8859-1')
nombres_df = pd.read_csv(r'C:\Users\hdzdi\OneDrive\Escritorio\Electores4.csv', encoding='ISO-8859-1')
print("en proceso...")


# Preparación de datos
n_registros = 3250000  # Ajusta esto según el número de registros que necesites
clave_elector = range(74750001, 74750001 + n_registros)
nombres = [f"{nombre} {apellido}" for nombre, apellido in zip(nombres_df['NOMBRE'], nombres_df['APELLIDO'])]
genero = nombres_df['GENERO'].tolist()

print("preparación:")
print("Longitud de 'clave_elector':", len(clave_elector))
print("Longitud de 'nombres':", len(nombres))
print("Longitud de 'genero':", len(genero))

# Generación aleatoria de domicilios y otros campos
estado_id = np.random.choice(entidades_df['ENTIDAD'], n_registros)
municipio_id = np.random.choice(municipios_df['MUN'], n_registros)
localidad_id = np.random.choice(localidades_df['LOC'], n_registros)

domicilio = [
    f"{entidades_df.loc[entidades_df['ENTIDAD'] == estado, 'NOM_ENT'].values[0]} "
    f"{municipios_df.loc[municipios_df['MUN'] == municipio, 'NOM_MUN'].values[0]} "
    f"{localidades_df.loc[localidades_df['LOC'] == localidad, 'NOM_LOC'].values[0]} Calle #{np.random.randint(1, 1000)}"
    for estado, municipio, localidad in zip(estado_id, municipio_id, localidad_id)
]

casilla_id = estado_id + np.random.randint(1, 4901, n_registros)
ha_votado = np.random.choice([0, 1], p=[0.47, 0.53], size=n_registros)
condicion_penal = ['ninguna'] * n_registros
centro_penitenciario_id = [None] * n_registros
consulado_id = [None] * n_registros
funcionario_de_casilla_id = np.random.choice([0, 1], p=[0.89, 0.11], size=n_registros)


print("ya mero...")


# Creación del DataFrame final
electores_df = pd.DataFrame({
    'clave_elector': clave_elector,
    'nombre': nombres[:n_registros],  # Asegura tener suficientes nombres
    'genero': genero[:n_registros],
    'domicilio': domicilio,
    'estado_id': estado_id,
    'municipio_id': municipio_id,
    'alcaldia_id': municipio_id,  # Asume igual a municipio_id; ajustar si necesario
    'casilla_id': casilla_id,
    'ha_votado': ha_votado,
    'condicion_penal': condicion_penal,
    'centro_penitenciario_id': centro_penitenciario_id,
    'consulado_id': consulado_id,
    'localidad_id': localidad_id,
    'funcionario_de_casilla_id': funcionario_de_casilla_id
})

# Exportación a CSV
ruta_salida = r'C:\Users\hdzdi\OneDrive\Escritorio\electores_pt4.csv'
electores_df.to_csv(ruta_salida, index=False, encoding='ISO-8859-1')

print("Archivo 'electores.csv' generado con éxito.")
