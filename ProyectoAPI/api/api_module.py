import pandas as pd
from sodapy import Socrata

def consulta_covid(nombre_departamento, limite_regristros):
    """Consulta los casos de COVID-19 en un departamento especifico de Colombia utilizando la API de Datos Abiertos.

    Args:
        nombre_departamento: Nombre del departamento a consultar.
        limite_regristros: Numero maximo de registros a obtener.

    Returns:
        pandas.DataFrame: Un DataFrame que contiene los resultados de la consulta con las columnas seleccionadas.
        None: Si no se encontraron registros para el departamento especificado.
    """
    
    #Conexion con la API de Datos Abiertos
    client = Socrata("www.datos.gov.co", None)
    
    #Consulta a la API con los parametros ingresados
    resultados = client.get("gt2j-8ykr", limit=limite_regristros, departamento_nom=nombre_departamento)
    
    #Convertir los resultados a un DataFrame de pandas
    df = pd.DataFrame.from_records(resultados)
    
    #Verificar si el DataFrame esta vacio
    if df.empty:
        print(f"👎❌No se encontraron registros para el departamento '{nombre_departamento}'.")
        return None  #Retorna None si no hay registros
    
    #Seleccion de columnas requeridas
    columnas_requeridas = ["ciudad_municipio_nom", "departamento_nom", "edad", "fuente_tipo_contagio", "estado"]
    df = df[columnas_requeridas]
    
    #Renombre de las columnas requeridas
    df.columns = ["Ciudad", "Departamento", "Edad", "Tipo de Contagio", "Estado"]
    
    return df
    