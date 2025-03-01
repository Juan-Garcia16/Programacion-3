from tabulate import tabulate

def obtener_datos_usuario():
    """Solicita al usuario el nombre de un departamento y un limite de registros para consultar casos de COVID-19 en Colombia."""
    print("🤧Consulta de casos de COVID-19🦠 en Colombia😷 ")
    
    #Ingreso de datos
    departamento = input("Ingrese el nombre del departamento a consultar: ").upper()
    limite = int(input("Ingrese el numero de registros a obtener: "))
    
    return departamento, limite


def mostrar_resultados(dataframe):
    """Muestra los resultados de la consulta en formato de tabla.
    
    Args: 
        dataframe: Un DataFrame que contiene los resultados de la consulta."""
    print("\n✅Resultados de la consulta:\n")
    
    #Mostrar los resultados en formato de tabla
    print(tabulate(dataframe, headers="keys", tablefmt="pretty", showindex=False, stralign="left"))

