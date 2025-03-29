from sodapy import Socrata

# Conectarse a la API (sin autenticación)
client = Socrata("www.datos.gov.co", None)

# Hacer una consulta pequeña (solo 3 registros para prueba)
resultados = client.get("gt2j-8ykr", limit=3, departamento_nom="RISARALDA")



# Imprimir los datos sin formato para ver su estructura
print(resultados)

'''
Ciudad de ubicación
Departamento
Edad
Tipo
Estado
País de procedencia'''