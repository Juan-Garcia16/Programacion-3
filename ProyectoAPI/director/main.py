import sys
import os

#Anadimos la carpeta raíz del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.api_module import consulta_covid
from ui.ui_module import obtener_datos_usuario, mostrar_resultados

def main():
    """Funcion principal del programa que coordina obtencion de datos ingresados, cosulta a la API, y muestra de resultados en pantalla."""
    
    #Obtener datos del usuario
    departamento, limite = obtener_datos_usuario()
    
    #Consultar la API
    datos = consulta_covid(departamento, limite)
    
    #Mostrar los resultados
    if datos is not None:
        mostrar_resultados(datos)
    
if __name__ == "__main__":
    main()