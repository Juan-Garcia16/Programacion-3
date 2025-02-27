from tabulate import tabulate

def obtener_datos_usuario():
    print("🤧Consulta de casos de COVID-19🦠 en Colombia😷 ")
    
    #Ingreso de datos
    departamento = input("Ingrese el nombre del departamento a consultar: ").upper()
    limite = int(input("Ingrese el numero de registros a obtener: "))
    
    return departamento, limite

def mostrar_resultados(dataframe):
    print("\n✅Resultados de la consulta:\n")
    print(tabulate(dataframe, headers="keys", tablefmt="pretty", showindex=False, stralign="left"))
    #print(dataframe.to_string(index=False))