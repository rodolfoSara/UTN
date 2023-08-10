import re

menu='''
1 Corroborar mayúscula
2 Corroborar minúscula
3 Corroborar si es número entero
4 Corroborar si es sólo texto
5 Corroborar si es número decimal
6 Corroborar si es numero y/o texto
7 Corroborar si es binario
8 Palabras que comiencen con la letra U
9 Palabras entre 3 y 6 letras
10 Palabras que terminan con ‘ción’
11 Palabras que comienzan con vocal
12 Dividir cadena 
13 Corregir texto
14 Validar formato fecha
15 Validar formato hora
16 Validad código postal
17 Validar patente de auto
18 Obtener Mails
19 Validar Password
20 Validar IP
21 Salir
'''

'''
1. Crear una función llamada es_mayuscula que reciba un string y devuelva True
en caso de que todas las letras sean mayúsculas o False en el caso contrario
'''
def es_mayuscula(cadena:str):
    if cadena.isupper():
        return True
    else:
        return False

'''
2. Crear una función llamada es_minuscula que reciba un string y devuelva True
en caso de que todas las letras sean mayúsculas o False en el caso contrario
'''
def es_minuscula(cadena:str):
    if cadena.islower():
        return True
    else:
        return False
'''
3. Crear una función llamada es_entero que reciba un string y devuelva True en
caso de que se trate de un número entero y False en caso contrario.
'''
def es_entero(cadena:str):
    if cadena.isnumeric():
        return True
    else:
        return False

'''
4. Crear una función llamada es_solo_texto que reciba un string y devuelva True
en caso de que trate solo de caracteres alfabéticos y el espacio y False en el
caso contrario
'''
def es_solo_texto(cadena:str):
    contador = 0
    lista = cadena.split()
    for i in range(len(lista)):
        print(lista[i])
        if lista[i].isalpha():
            contador += 1

    if contador == len(lista):
        return True
    return False

'''
5. Crear una función llamada es_decimal que reciba dos strings: el primero
representa la expresión a evaluar y el segundo el separador decimal (puede
ser punto . o coma ,). Debe devolver True en caso que se trate de un número
decimal y False en el caso contrario.'''
def es_decimal(numero:str, separador:str):
    try:
        numero = numero.replace(separador, '.')
        float(numero)
        return True

    except ValueError:
        return False

'''
Crear una función llamada es_alfanumerico que devuelva True en caso de
tratarse de solo letras y números y False en el caso contrario (es decir que
contenga caracteres especiales)
'''
def es_alfanumerico(cadena:str):
        cadena = cadena.replace(" ", "")
        if cadena.isalnum():
            return True
        return False

'''
7. Crear una función llamada es_binario que devuelva True en caso de un
número binario válido (solo ceros y unos) o False en el caso contrario
'''
def es_binario(numero):

    patron = r"[^01]"
    resultado = re.search(patron, numero)

    if resultado:
        return False
    else:
        return True

'''
8. Crear una función que reciba una lista de palabras y devuelva otra lista con
las palabras que comienzan con la letra ‘U’
'''
def comienza_con_u(lista:list):
    u_lista = []
    for i in lista:
        if i[0] == 'u':
            u_lista.append(i)
    return u_lista

'''
9. Crear una función que reciba un texto y devuelva una lista con las palabras
que contienen entre 3 y 6 caracteres de largo
'''
def palabras_entre_tres_y_seis(cadena:str):
    lista = []
    cadena = cadena.split()
    for i in cadena:
        if len(i) >= 3 and len(i) <= 6:
            lista.append(i)
    return lista

'''
10. Crear una función que reciba un texto y devuelva una lista de todas las
palabras que terminan con ‘ción’.
'''
def palabras_cion(cadena:str):
    palabras = []
    cadena = cadena.split()
    for i in cadena:
        if i[-4:] == 'ción':
            palabras.append(i)
    return palabras

'''
11. Crear una función que reciba un texto y devuelva una la lista de palabras
encuentra que comienzan con una vocal
'''
def palabras_vocal(cadena:str):
    vocales =['a', 'e', 'i', 'o', 'u']
    palabras = []
    cadena = cadena.split()
    for i in cadena:
        if i[0] in vocales:
            palabras.append(i)
    return palabras
'''
12. Crear una función llamada obtener_oraciones que reciba como parámetro un
string y que devuelva una lista con las oraciones (delimitadores, ‘.’, ‘!’, ‘?’).
'''
def obtener_oraciones(cadena:str):
    lista = []
    lista = re.split("[.|!|?]", cadena)
    return lista
# ‘.’, ‘!’, ‘?’).

'''
13. Crear una función que reciba un texto como parámetro y que corrija los
errores de ortografía que no cumplan con la regla ortográfica que indica que
antes de V se escribe N y que antes de B se escribe M.
'''
def corregir (cadena:str):
    corregido = re.sub('mv', 'nv', cadena)
    return corregido

'''
14. Crear la función es_fecha que reciba dos string, el primero representa la
expresión a evaluar y el segundo el separador de la fecha (puede ser la barra /
o el guión -) y que devuelva True en caso de tratarse de una fecha válida y
False en el caso contrario. Los formatos admitidos son: ‘dd/mm/aaaa’ o
‘dd-mm-aaaa’'''
def es_fecha(cadena:str, separador:str):
    fecha = ""
    cadena = cadena.split()
    for i in range(len(cadena) - 1):
        fecha += cadena[i] + separador
    fecha += cadena[-1]
    comprobar = re.match("([0-9]{2})(\/|\-)([0-9]{2})(\/|\-)([0-9]{4})", fecha)

    if comprobar:
        return True
    return False

    print(comprobar)

'''
15. Crear la función es_hora que reciba un string y que devuelva True en caso de
tratarse de una hora válida y False en el caso contrario. El formato admitido
es ‘hh:mm:ss’
'''
def es_hora(hora:str):
    comprobar = re.match("([0-9]{2}):([0-9]{2}):([0-9]{2})", hora)
    if comprobar:
        return True
    return False

'''
16. Crear la función validar_codigo_postal que reciba un string como parámetro y
devuelva True en caso de tratarse de código postal válido o False en caso
contrario.
'''
def validar_codigo_postal(codigo_postal:str):
    comprobar = re.match("([A-Z]){1}(\d){4}([A-Z)]){3}", codigo_postal)
    if comprobar:
        return True
    return False

'''
17. Crear la función validar_patente que reciba un string como parámetro y
devuelva True en caso de tratarse de un número de patente válido o False en
caso contrario.
'''
def validar_patente(patente:str):
    comprobar1 = re.match("([A-Z]){2}\s([0-9]{3})\s([A-Z]){2}", patente)
    comprobar2 = re.match("([A-Z]){3}\s([0-9]{3})", patente)
    if comprobar1 or comprobar2:
        return True
    return False

'''
18. Crear una función que se llame obtener_direcciones_email que reciba un texto
y devuelva una lista con todas las direcciones de email válidas que
encuentren en el mismo.
'''
def obtener_direcciones_email(cadena:str):
    lista_mail = []
    cadena = cadena.split()
    for i in cadena:
        comprobar = re.match("([a-z]){1,}@([a-z]){1,}.([a-z]){1,}.([a-z]){1,}?", i)
        if comprobar:
            lista_mail.append(i)
    return lista_mail

'''
○ Al menos 8 caracteres
○ Al menos una letra mayúscula y una letra minúscula
○ Un número
○ Un carácter especial'''
def validar_password(pasword:str):
    if len(pasword) < 8:
        return False
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

'''
20. Crear una función llamada validar_ip que reciba un string como parámetro y
verifique si se trata de una dirección IP v4 válida, en caso de serlo retornar
True de lo contrario retornar False.
Se considera una dirección IP válida si tiene el formato xxx.xxx.xxx.xxx, donde
xxx es un número entero entre 0 y 255.
'''
def validar_ip(ip:str):
    if not re.search(r'(\d){1,3}.(\d){1,3}.(\d){1,3}.(\d){1,3}', ip):
        return False

    ip = ip.split('.')
    print(ip)
    for i in ip:
        if int(i) < 0 or int(i) > 255:
            return False


    return True


while True:
    print(menu)
    option = int(input('Seleccione una opción '))

    match(option):
        case 1:
            cadena = input('Escriba un texto ')
            print(f"Es mayúscula: {es_mayuscula(cadena)}")
        case 2:
            cadena = input('Escriba un texto ')
            print(f"Es minúscula: {es_minuscula(cadena)}")
        case 3:
            cadena = input('Escriba un texto ')
            print(f"Es entero: { es_entero(cadena)}")
        case 4:
            cadena = input('Escriba un texto ')
            print(f"Es solo texto: {es_solo_texto(cadena)}")
        case 5:
            numero = input('Escriba un numero ')
            separador = input('Escriba si quiere con . o , el decimal ')
            print(f"Es decimal: {es_decimal(numero, separador)}")
        case 6:
            cadena = input('Escriba un texto ')
            print(f"Es decimal: {es_alfanumerico(cadena)}")
        case 7:
            cadena = input('Escriba un texto ')
            print(f"Es decimal: { es_binario(cadena)}")
        case 8:
            lista = ['Hola', 'uva', 'uber', 'perro']
            print(f"Palabras que comiencen con la letra U {comienza_con_u(lista)}")
        case 9:
            cadena = input('Escriba un texto ')
            print(f"Palabras que comiencen con la letra U {palabras_entre_tres_y_seis(cadena)}")
        case 10:
            cadena = "La tecnología de la información ha revolucionado la comunicación en todas sus formas. La digitalización y la automatización de procesos han permitido la optimización de los recursos y la mejora en la eficiencia de los sistemas. La cibernética, la robótica y la inteligencia artificial son algunas de las áreas de la informática que se han desarrollado en las últimas décadas y han transformado la forma en que vivimos y trabajamos. La interconexión de dispositivos y la transmisión de datos en tiempo real han permitido la creación de nuevas industrias y modelos de negocio que antes eran impensables. La educación, la salud, el transporte y la logística son algunos de los sectores que han sido beneficiados por la innovación tecnológica. En conclusión, la tecnología ha generado una revolución en nuestra sociedad que ha llevado a la transformación y evolución de la misma."
            print(f"Palabras q termina con ción: {palabras_cion(cadena)}")
        case 11:
            cadena = "La tecnología de la información ha revolucionado la comunicación en todas sus formas. La digitalización y la automatización de procesos han permitido la optimización de los recursos y la mejora en la eficiencia de los sistemas. La cibernética, la robótica y la inteligencia artificial son algunas de las áreas de la informática que se han desarrollado en las últimas décadas y han transformado la forma en que vivimos y trabajamos. La interconexión de dispositivos y la transmisión de datos en tiempo real han permitido la creación de nuevas industrias y modelos de negocio que antes eran impensables. La educación, la salud, el transporte y la logística son algunos de los sectores que han sido beneficiados por la innovación tecnológica. En conclusión, la tecnología ha generado una revolución en nuestra sociedad que ha llevado a la transformación y evolución de la misma."
            print(f"Palabras q termina con ción: {palabras_vocal(cadena)}")
        case 12:
            cadena = "¿Bello es mejor que feo? Explícito es mejor que implícito? Simple es mejor que complejo. " \
                     "Complejo es mejor que complicado. Plano es mejor que anidado. Espaciado es mejor que denso. " \
                     "La legibilidad es importante. Los casos especiales no son lo suficientemente especiales" \
                     " como para romper las reglas. Sin embargo la practicidad le gana a la pureza. " \
                     "Los errores nunca deberían pasar silenciosamente. A menos que se silencien explícitamente. " \
                     "Frente a la ambigüedad, evitar la tentación de adivinar. Debería haber una," \
                     " y preferiblemente solo una, manera obvia de hacerlo. A pesar de que eso no sea obvio al principio a menos que seas Holandés. Ahora es mejor que nunca. A pesar de que nunca es muchas veces mejor que *ahora* mismo. Si la implementación es difícil de explicar, es una mala idea. Si la implementación es fácil de explicar, puede que sea una buena idea. Los espacios de nombres son una gran idea, ¡tengamos más de esos!"

            print(obtener_oraciones(cadena))
        case 13:
            cadena = "Mi comvicción me hace sentir que es el momento " \
                     "de imvertir tiempo para finalmente envarcar en esta nueva aventura."

            print(corregir(cadena))

        case 14:
            dia = input('Escriba un dia ')
            if int(dia) < 10:
                dia = '0' + dia
            mes = input('Escriba un mes ')
            if int(mes) < 10:
                mes = '0' + mes
            anio = input('Escriba un año ')
            separador = input('Escriba separador / o - ')
            cadena = dia + " " + mes + " "  + anio
            print(es_fecha(cadena, separador))
        case 15:
            hora = input('Escriba la hora ')
            print(es_hora(hora))
        case 16:
            codigo_postal = input('Escriba código postal ')
            print(F"Es código postal: {validar_codigo_postal(codigo_postal)}")
        case 17:
            patente = input('Escriba código postal ')
            print(f"Es patente valida: {validar_patente(patente)}")
        case 18:
            cadena = " <Alberto, Cervantes> acervantes@gmx.com <Ana, Jimenez> ajimenez@hotmail.com <Antonio, Castillo> acastillo@gmail.com <Armando, Vega> avega@yahoo.com <Arturo, Arredondo> aarredondo@gmail.com <Beatriz, Vargas> bvargas@outlook.com <Berenice, Rios> bribos@yahoo.com <Brenda, Gonzalez> bgonzalez@terra.com <Brian, Hernandez> bhernandez@outlook.com <Camila, Reyes> creyes@terra.com <Carlos, Gallegos> cgallegos@gmail.com <Carolina, Alvarado> calvarado@outlook.com <Cesar, Rosales> crosales@terra.com <Christian, Moreno> cmoreno@gmail.com <Clara, Serrano> cserrano@yahoo.com <Cristian, Huerta> chuerta@terra.com <Cristina, Ochoa> cochoa@yahoo.com <Dalia, Rivas> drivas@outlook.com <Daniel, Perez> dperez@yahoo.com <Daniela, Ruiz> druiz@outlook.com <David, Velasco> dvelasco@gmail.com <Diana, Andrade> dandrade@yahoo.com <Diego, Ortiz> dortiz@terra.com <Eduardo, Vazquez> evazquez@gmail.com <Elisa, Castillo> ecastillo@outlook.com <Elizabeth, Cruz> ecruz@yahoo.com <Emmanuel, Pacheco> epacheco@terra.com <Enrique, Fuentes> efuentes@gmail.com <Erika, Cabrera> ecabrera@yahoo.com <Erick, Zavala> ezavala@outlook.com <Esmeralda, Valdes> evaldes@gmx.com <Esteban, Montes> emontes@gmail.com <Evelyn, Vera> evera@yahoo.com <Fabian, Rangel> frangel@terra.com <Fatima, De La Cruz> fdela@gmx.com <Felipe, Salas> fsalas@outlook.com <Fernanda, Guerrero> fguerrero@gmail.com <Fernando, Olvera> folvera@yahoo.com <Francisco, Hernandez> fhernandez@terra.com <Gabriela, Acosta> gacosta@gmail.com <Gael, Maldonado> gmaldonado@outlook.com <Gerardo, Flores> gflores@yahoo.com <Giselle, Alvarado> galvarado@terra.com <Gloria, Tapia> gtapia@gmx.com <Gonzalo, Zamora> gzamora@yahoo.com <Graciela, Ochoa> gochoa@outlook.com <Guadalupe, Aguilar> gaguilar@gmail.com <Guillermo, Garza> ggarza@yahoo.com <Gustavo, Mora> gmora@terra.com <Heidi, Hernandez> hhernandez@gmx.com <Hector, Barrios> hbarrios@outlook.com <Hugo, Villarreal> hvillarreal@yahoo.com <Ignacio, Soto> isoto@gmail.com <Ingrid, Vidal> ividal@yahoo.com <Irma, Garza> igarza@terra.com <Isaac, Palacios> ipalacios@gmail.com <Ivan, Rojas> irojas@yahoo.com <Jacqueline, Fuentes> jfuentes@outlook.com <Jaime, Huerta> jhuerta@yahoo"
            print(obtener_direcciones_email(cadena))
        case 19:
            password = input('Escriba su password ')

            if validar_password(password):
                print("La contraseña es válida.")
            else:
                print("La contraseña no cumple con los requisitos mínimos de seguridad.")
        case 20:
                ip = input('Escriba una IP ')
                print(validar_ip(ip))
        case 21:
            break
        case _:
            print('Error')

