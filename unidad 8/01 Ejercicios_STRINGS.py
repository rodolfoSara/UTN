import re

menu='''
1 Convertir a mayáscula
2 Convertir a minúscula
3 Concatenar dos cadenas
4 Contar caracteres
5 Contar caractere en particular
6 Encontrar palabras que contienen un caracter
7 Quitar espacios de la cadena
8 Nombre y apellido en diccionario
9 Separar una lista
10 Armar un mail
11 De lista a Cadena
12 Número de tarjeta de crédito
13 Tomar usuario de mail
14 NO HICE
15 Cadena sin símbolos
16 COnvertir cadena en acronimo
17 Convertir a binario
18 Reemplazar mayúsculas por minúscular y viceversa
19 Contar digitos
20 Mail pasado a cadena
21 Contar apariciones de palabra
22 Salir
'''


'''
1. Escribir una función que reciba un string y devuelva el mismo string todo en
mayúsculas.
'''
def mayuscula(cadena:str):
    cadena = cadena.upper()
    return cadena

'''
2. Escribir una función que reciba un string y devuelva el mismo string todo en
minúsculas.'''
def minuscula(cadena:str):
    cadena = cadena.lower()
    return cadena
'''
3. Escribir una función que tome dos strings y devuelva un nuevo string que
contenga ambos strings concatenados, separados por un espacio.
'''
def concatenar(cadena1:str, cadena2:str):
    concatenado = cadena1 + ' ' + cadena2
    return  concatenado
'''Escribir una función que tome un string y devuelva el número de caracteres
que tiene el string.
'''
def contarCaracteres(cadena:str):
    contador = 0
    for i in cadena:
        if i.isalnum():
            contador += 1
    return contador
'''
5. Escribir una función que tome un string y un carácter y devuelva el número de
veces que aparece ese carácter en el string.
'''
def contarCaracter(cadena:str, caracter:str):
    contador = 0
    for i in cadena:
        if i == caracter:
            contador += 1
    return contador

'''
6. Escribir una función que tome un string y un carácter y devuelva una lista con
todas las palabras en el string que contienen ese carácter.
'''
def palabrasCaracter(cadena:str, caracter:str):
    lista = []
    cadena = cadena.split()
    for i in cadena:
        for j in i:
            if j == caracter:
                lista.append(i)
    return lista
'''
7. Escribir una función que tome un string y devuelva el mismo string con los
espacios eliminados
'''
def quitarEspacios(cadena:str):
    cadena = cadena.replace(" ","")
    return cadena

'''
8. Escribir una función que reciba dos string (nombre y apellido) y devuelva un
diccionario con el nombre y apellido, eliminando los espacios del comienzo y
el final y colocando la primer letra en mayúscula
'''
def nombreApellido(nombre:str, apellido:str):
    nombre_apellido_Dict = {}
    nombre = nombre.strip()
    nombre = nombre.capitalize()
    apellido = apellido.strip()
    apellido = apellido.capitalize()
    nombre_apellido_Dict['Nombre'] = nombre
    nombre_apellido_Dict['Apellido'] = apellido
    return nombre_apellido_Dict

'''
9. Escribir una función que tome una lista de nombres y los una en una sola
cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"]
-> "Juan\nMaría\nPedro".
'''
def listaSeparada(lista:list):
    cadena = ""
    for i in lista:
        cadena += i + "\n"
    print(cadena)
'''
10. Escribir una función que tome un nombre y un apellido y devuelva un email en
formato "inicial_nombre.apellido@utn-fra.com.ar".
'''
def armarMail(nombre:str, apellido:str):
    mail = f"{nombre}{apellido}@utn-fra.com.ar"
    return mail
'''
11. Escribir una función que tome una lista de palabras y devuelva un string que
contenga todas las palabras concatenadas con comas y "y" antes de la última
palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el
string resultante debería ser "manzanas, naranjas y bananas"..
'''
def listaAstring(lista:list):
    cadena =""
    for i in range(len(lista) - 1):
        cadena += lista[i] + ", "
    cadena += "y " + lista[-1]
    return cadena

'''
12. Escribir una función que tome un número de tarjeta de crédito como input,
verificar que todos los caracteres sean numéricos y devolver los últimos
cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** ****
**** 1234".
'''
def tarjeta_credito(numero_tarjeta:int):
    if not numero_tarjeta.isdigit():
        raise ValueError("El número de tarjeta de crédito debe contener sólo dígitos numéricos.")

    primero_digitos = numero_tarjeta[:-4]
    primero_digitos = len(primero_digitos) * "*"
    ultimo_digitos =numero_tarjeta[-4:]

    cadena =""
    for i in range(0, len(primero_digitos), 4):
        cadena += "**** "
    cadena += " " + ultimo_digitos
    return cadena

'''
13. Escribir una función que tome un correo electrónico y elimine cualquier
carácter después del símbolo @, por ejemplo: "usuario@gmail.com" ->
"usuario".
'''
def tomarMail(mail:str):
    busqueda = re.search(r'^[a-zA-Z]{0,200}', mail)
    return busqueda


'''
14. Escribir una función que tome una URL y devuelva solo el nombre de dominio,
por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..
'''
def tomarWeb(web:str):
    busqueda = re.search(r'[^(https?:\/\/)?(www\.)?]')
    print(busqueda)

'''
15. Escribir una función que tome una cadena de texto y devuelva solo los
caracteres alfabéticos, eliminando cualquier número o símbolo, por ejemplo:
"H0l4, m4nd0!" -> "Hl, mnd.
'''
def es_caracter(cadena:str):
    cadenaSinSimbolos =""
    for i in cadena:
        if i.isalpha():
            cadenaSinSimbolos += i
        elif i == " ":
            cadenaSinSimbolos += i
    return cadenaSinSimbolos

'''
16. Escribir una función que tome una cadena de texto y la convierta en un
acrónimo, tomando la primera letra de cada palabra, por ejemplo:
"Universidad Tecnológica Nacional Facultad Regional Avellaneda" ->
"UTNFRA”.
'''
def a_acronimo (cadena:str):
    acronimo = ""
    cadena = cadena.split()
    for i in cadena:
        acronimo += i[0]
    return acronimo
'''
17. Escribir una función que tome un número binario y lo convierta en una cadena
de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo:
"101" -> "00000101".
'''
def convertir_binario(cadena:str):
    cadena = cadena.zfill(8)
    return cadena
'''
18. Escribir una función que tome una cadena de caracteres y reemplace todas
las letras mayúsculas por letras minúsculas y todas las letras minúsculas por
letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"
'''
def may_min_cambio(cadena:str):
    cadena_cambiada = ""
    for i in cadena:
        for j in i:
            if j.isupper():
                j = j.lower()
            else:
                j= j.upper()
            cadena_cambiada += j
    return cadena_cambiada

'''
19. Escribir una función que tome una cadena de caracteres y cuente la cantidad
de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.
'''
def contar_digitos(cadena:str):
    contador = 0
    for i in cadena:
        for j in i:
            if j.isnumeric():
                contador +=1
    return contador


'''
20. Escribir una función que tome una lista de direcciones de correo electrónico y
las una en una sola cadena separada por punto y coma, por ejemplo:
["juan@gmail.com", "maria@hotmail.com"] ->
"juan@gmail.com;maria@hotmail.com".
'''
def lista_a_cadena(lista:list):
    cadena = ""
    for i in range(len(lista) - 1):
        cadena += lista[i] + ", "

    if len(lista) > 1:
        cadena += lista[-1]
    return cadena

'''
21. Crear una función que reciba como parámetro un string y devuelva un
diccionario donde cada clave es una palabra y cada valor es un entero que
indica cuántas veces aparece esa palabra dentro del string.'''
def contar_palabra(cadena:str):
    contar_palabras_dict ={}
    cadena = cadena.split()
    for i in cadena:
        if i in contar_palabras_dict:
            contar_palabras_dict[i] += 1
        else:
            contar_palabras_dict[i] = 1
    return contar_palabras_dict

while True:
    print(menu)
    option = int(input('Elija una opción '))

    match(option):
        case 1:
            cadena = input('Escriba un texto para convertir a mayúscula ')
            print(mayuscula(cadena))
        case 2:
            cadena = input('Escriba un texto para convertir a minúscula ')
            print(minuscula(cadena))

        case 3:
            cadena1 = input('Escriba un texto para concatenar ')
            cadena2 = input('Escriba un texto para concatenar ')
            print(concatenar(cadena1, cadena2))
        case 4:
            cadena = input('Escriba un texto para contar caracteres ')
            print(contarCaracteres(cadena))
        case 5:
            cadena = input('Escriba un texto para contar caracteres ')
            caracter = input('Escriba el caracter a contar ')
            print(contarCaracter(cadena, caracter))
        case 6:
            cadena = input('Escriba un texto para encontrar caractere ')
            caracter = input('Escriba el caracter a encontrar ')
            print(palabrasCaracter(cadena, caracter))
        case 7:
            cadena = input('Escriba un texto para quitar espacios ')
            print(quitarEspacios(cadena))
        case 8:
            nombre = input('Escriba un nombre ')
            apellido = input('Escriba apellido ')
            print(nombreApellido(nombre, apellido))
        case 9:
            lista = ["Juan", "María", "Pedro"]
            listaSeparada(lista)
        case 10:
            nombre = input('Escriba un nombre ')
            apellido = input('Escriba apellido ')
            print(armarMail(nombre, apellido))
        case 11:
            lista = ["manzanas", "naranjas", "bananas"]
            print(listaAstring(lista))
        case 12:
            numero_tarjeta = input('Escriba número ')
            print(tarjeta_credito(numero_tarjeta))
        case 13:
            mail = input('Escriba mail')
            print(tomarMail(mail))
        case 14:
            pass
        case 15:
            cadena = input('Escriba un texto para quitar símbolos  ')
            print(es_caracter(cadena))
        case 16:
            cadena = input('Escriba un texto para convertir en acronimo ')
            print(a_acronimo(cadena))
        case 17:
            cadena = input('Escriba un numero binario (hasta 8 bits) ')
            print(convertir_binario(cadena))
        case 18:
            cadena = input('Escriba una frase para cambiar mayúsculas y minúsculas ')
            print(may_min_cambio(cadena))
        case 19:
            cadena = input('Escriba texto para contar los dígitos')
            print(f"La cantidad de dígitos en la cadena es {contar_digitos(cadena)}")
        case 20:
            lista = ["juan@gmail.com", "maria@hotmail.com"]
            print(lista_a_cadena(lista))
        case 21:
            cadena = '''
            21. Crear una función que reciba como parámetro un string y devuelva un
            diccionario donde cada clave es una palabra y cada valor es un entero que
            indica cuántas veces aparece esa palabra dentro del string.'''
            print(contar_palabra(cadena))
        case 22:
            break