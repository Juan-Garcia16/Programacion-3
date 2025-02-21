"""begin{question}{1}
Para este ejercicio debe crear un programa que calcule las estaturas (\textit{interos, dobles}) promedio de un salón de clase. El usuario debe de ingresar el número cero (como una \textit{variable sentinela} de manera que pueda indicar que ya no desea ingresar mas datos)."""

"""
estaturas = []

while (True):
    estatura = float(input("Ingrese una estatura (0 para terminar de registrar): "))
    if estatura == 0:
        break
    else:
        estaturas.append(estatura)

#Valida si la estructura esta vacia
if estaturas:
    print(f"El promedio de estaturas es: {sum(estaturas) / len(estaturas):.2f}")
else:
    print("No se ingresaron estaturas.")
"""
#-------------------------------------------------------------------------------
"""Modifique el ejercicio anterior esta vez en lugar de digitar el número cero para indicar que se desea parar de ingresar estaturas usted debe de mostrar en pantalla el mensaje ``Desea ingresar mas estaturas [S/N]''. Utilice la respuesta obtenida para detener el ciclo."""
'''
estaturas = []

while (True):
    estatura = float(input("Ingrese una estatura: "))
    estaturas.append(estatura)
    a = input("Desea ingresar mas estaturas [S/N]: ")
    a = a.lower()
    
    if a == "n":
        break
    elif a != "s":
        print("Respuesta no valida, ingrese 'S' o 'N'.")
        
#Valida si la estructura esta vacia
if estaturas:
    print(f"El promedio de estaturas es: {sum(estaturas) / len(estaturas):.2f}")
else:
    print("No se ingresaron estaturas.")
'''
#-------------------------------------------------------------------------------
'''Escriba un programa que muestre una tabla de conversión de temperatura para grados Celsius y grados Fahrenheit. La tabla debe incluir filas para todas las temperaturas entre 0 y 100 grados Celsius que sean múltiplos de 10 grados Celsius. Incluya títulos apropiados en sus columnas.'''

'''
print("\tConversion grados celsius a Fahrenheit\n")
print("Celsius | Fahrenheit")
print("---------------------")

for i in range(11):
    celsius = i*10
    celsius_Fahrenheit = celsius*(9/5) + 32
    print(celsius, "\t|", celsius_Fahrenheit)
'''
#-------------------------------------------------------------------------------
'''Un auto cinema tiene un rango de precios para el ingreso a sus funciones. De 3 años o menos son admitidos sin cargo. Entre 3 y 11 años el valor de su entrada es \$16.00. Los adultos mayores de 50 años y más cuestan \$40.00. El valor de la entrada para todos los demás cuesta \$34.00.\\

Usted debe de crear un programa que lea las edades de cada pasajero del automóvil y calcule el valor total de la entrada. El costo debe mostrarse usando dos decimales.'''

'''
total = 0

for i in range(4):
    pasajero = int(input(f"Ingrese edad del pasajero {i+1}: "))
    if pasajero <= 3:
        total += 0
    elif pasajero > 3 and pasajero <= 11:
        total += 16.00
    elif pasajero > 50:
        total += 40.00
    else:
        total += 34.00
        
print(f"El costo de la entrada al cinema para el automovil es: ${total:.2f}")
'''
#-------------------------------------------------------------------------------
'''Se tiene una lista que contiene los códigos de los empleados de un almacen. Sin embargo, alguien registró erroneamente registros duplicados ['ref-010', 'ac-090','ref-010','xp-89','as-65','kj-11','xp-89', 'wx-23','rk-87','as-65']. Usted debe de escribir un programa que permita eliminar los elementos duplicados.'''

'''
codigosEmpleados = ['ref-010', 'ac-090','ref-010','xp-89','as-65','kj-11','xp-89', 'wx-23','rk-87','as-65']
codigosEmpleadosSinDuplicado = list(set(codigosEmpleados))
        
print(codigosEmpleadosSinDuplicado)
'''
#-------------------------------------------------------------------------------
'''Escriba un programa donde el usuario digite una palabra y obtenga una lista con las consonantes de la palabra ingresada.'''

'''
vocales = "aeiouAEIOU"
palabra = input("Ingrese una palabra: ")
consonantes = []

for char in palabra:
    if char.isalpha() and char not in vocales:
        consonantes.append(char)

print("Su consonantes son: ")
print(consonantes)
'''
#-------------------------------------------------------------------------------
'''Según el plan de estudios de la Universidad un alumno puede matricular al mismo tiempo Programación III y Programación IV. Escriba un programa donde:

Cree una lista de asistencia por cada materia que almacene los alumnos matriculados.

El programa debe de generar una lista con los alumnos que tienen matriculadas Programación III y Programación IV simultáneamente.'''

'''
programacionIII = ["Juan", "David", "Alejandro", "Paula", "Pablo", "Matias", "Esteban"]
programacionIV = ["Carlos", "Isabella", "Martin", "Alejandra", "Alejandro", "Juan", "Paula", "Thomas"]

simultaneos = list(set(programacionIII) & set(programacionIV))
print(simultaneos)
'''
#-------------------------------------------------------------------------------
'''Es conocido que los elementos de una lista pueden ser de cualquier tipo; inclusive otra lista (ej: [3.14, ``Hola Doc!'', [911, ``Los chicos malos'']]). Escriba un programa que verifique si una lista contiene una sublista.'''

'''
tecnologias = ["python", 3, "github", "sql", ["ruby, tailwind, typescript, css"], "html"]

for sublista in tecnologias:
    if type(sublista) == list:
        print("La lista contiene la sublista: ", sublista)
'''
#-------------------------------------------------------------------------------
'''En el stock de un almacen se tiene las siguientes referencias:
Brocha & 500  \\
\hline
Espatula & 2000 \\
\hline
Pala & 54000 \\
\hline
Carretilla & 300000 \\
\hline
Casco & 55000 \\
\hline
Soldador & 230000 \\
\hline
Alicate & 10000 \\
\hline
Destornillador & 3000 \\
\hline
Maza & 60000 \\
\hline
Nivel & 24000 \\
\hline
Flexometro & 76000 \\
\hline
Hacha & 32000 \\
\hline
Pico & 74000 \\
\hline
Rastrillos & 56000\\
\hline

Escriba un programa que ordene este stock por su ``Producto'' '''

'''
stock = {"Brocha": 500, "Espatula": 2000, "Pala": 54000, "Carretilla": 300000, "Casco": 55000, "Soldador": 230000, "Alicate": 10000, "Destornillador": 3000, "Maza": 60000, "Nivel": 24000, "Flexometro": 76000, "Hacha": 32000, "Pico": 74000, "Rastrillos": 56000}

#comprension de diccionario
#{clave: valor for item in iterable}
stockOrdenado = {key: stock[key] for key in sorted(stock)}

print(stockOrdenado)
'''

'''Debe de crear una programa que almacene en una estructura la información contenida en la siguiente tabla:
\textbf{Banda} & \textbf{Miembros} \\
\hline
    Queen & Freddie Mercury, Brian May, Roger Taylor y John Deacon  \\
    \hline
    The Doors & Jim Morrison, Robby Krieger, Ray Manzarek y John Densmore \\
    \hline
    Green Day & Billie Joe Armstrong, Mike Dirnt  y Tré Cool  \\
    \hline
    Rolling Stones & Mick Jagger, Keith Richards, Charlie Watts y Ron Wood  \\
    \hline
    Led zeppelin & Robert Plant, Jimmy Page,  John Paul Jones y John Bonham.  \\
    \hline
    Black Sabbath & Ozzy Osbourne, Tony Iommi, Bill Ward y Geezer Butler \\
    \hline
    Soundgarden & Chris Cornell, Kim Thayil, Matt Cameron y Ben Shepherd. \\
    \hline
    Alice in Chains &  Layne Staley, Jerry Cantrell, Sean Kinney y Mike Starr \\
    \hline
    
Así mismo en programa debe:

\item Ordenar alfabéticamente la tabla y 
\item Mostrar en pantalla SOLAMENTE el vocalista de cada banda (que sería el primer nombre de los miembros de la misma) JUNTO con el nombre su respectiva banda.
'''

bandas = {
    "Queen": ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"],
    "The Doors": ["Jim Morrison", "Robby Krieger", "Ray Manzarek", "John Densmore"],
    "Green Day": ["Billie Joe Armstrong", "Mike Dirnt", "Tré Cool"],
    "Rolling Stones": ["Mick Jagger", "Keith Richards", "Charlie Watts", "Ron Wood"],
    "Led Zeppelin": ["Robert Plant", "Jimmy Page", "John Paul Jones", "John Bonham"],
    "Black Sabbath": ["Ozzy Osbourne", "Tony Iommi", "Bill Ward", "Geezer Butler"],
    "Soundgarden": ["Chris Cornell", "Kim Thayil", "Matt Cameron", "Ben Shepherd"],
    "Alice in Chains":["Layne Staley", "Jerry Cantrell", "Sean Kinney", "Mike Starr"],
}

bandasOrdendas = {k: bandas[k] for k in sorted(bandas)}
for banda, miembros in bandasOrdendas.items():
    vocalista = miembros[0]
    #ljust para cantidad de caracteres a ocupar
    print(f"Banda: {banda.ljust(18)}","|", f"Vocalista: {vocalista}")
    

