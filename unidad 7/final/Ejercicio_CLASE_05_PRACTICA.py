from data_stark import lista_personajes

menu='''
1 Imprimir nombre
2 Imprimir dato
3 Imprimir nombre y propiedad
4 Imprimir nombre y altura
5 Máximo y mínimo
6 Promedio
'''

def castear_float(lista_personajes, propiedad_float):
    casteado = 0
    if len(lista_personajes) > 0:
        for i in range(len(lista_personajes)):
           if type(lista_personajes[i][propiedad_float]) != float:
               lista_personajes[i][propiedad_float] = float(lista_personajes[i][propiedad_float])
               casteado += 1
           else:
               print(f'La {propiedad_float} del personaje {lista_personajes[i]["nombre"]} no se pudo castear')

    if casteado > 0:
        print(f' La propiedad {propiedad_float} están casteados')

def castear_int(lista_personajes, propiedad_int):
    casteado = 0
    if len(lista_personajes) > 0:
        for i in range(len(lista_personajes)):
           if type(lista_personajes[i][propiedad_int]) != int and lista_personajes[i][propiedad_int].isnumeric():
               lista_personajes[i][propiedad_int] = int(lista_personajes[i][propiedad_int])
               casteado += 1
           else:
               print(f'La {propiedad_int} del personaje {lista_personajes[i]["nombre"]} no se pudo castear')
    if casteado > 0:
        print(f' La propiedad {propiedad_int} están casteados')

castear_float(lista_personajes, 'altura')
castear_float(lista_personajes, 'peso')
castear_int(lista_personajes, 'fuerza')


for i in lista_personajes:
    print(i)

'''
1.2. Crear la función 'imprimir_dato' la cual recibirá por parámetro un string y
deberá imprimirlo en la consola. La función no tendrá retorno.
'''
def imprimir(lista_personajes, propiedad):
    if len(lista_personajes) > 0:
        for i in lista_personajes:
            if propiedad == "nombre":
                print(f'Nombre: {i["nombre"]}')
            else:
                print(f'{propiedad}: {i[propiedad]}')
    else:
        return -1


'''
2. Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un
diccionario el cual representara a un héroe y una key (string) la cual
representará el dato que se desea obtener.'''
def obtener_nombre_y_dato(lista_personajes:list, nombre:str, propiedad:str):
    if len(lista_personajes) > 0:
        for i in lista_personajes:
            if i['nombre'] == nombre:
               cadena =(f" Nombre: {i['nombre']} | {propiedad}: {i[propiedad]}")
    else:
        return -1
    return cadena

def stark_imprimir_nombres_alturas(lista_personajes:list):
    altura_nombre = []
    if len(lista_personajes) > 0:
        for i in lista_personajes:
            altura_nombre.append(obtener_nombre_y_dato(lista_personajes, i['nombre'], 'altura'))
    else:
        return -1
    return altura_nombre
'''
4.3. Crear la funcion 'calcular_max_min_dato' la cual recibira tres parámetros:
● La lista de héroes
● El tipo de cálculo a realizar: es un valor string que puede tomar los
valores ‘maximo’ o ‘minimo’
● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
‘peso’, ‘edad’, etc.
La función deberá retornar
'''
def calcular_max(lista_personajes:list, propiedad:str):
    indice = 0
    if len(lista_personajes) > 0:
        for i in range(len(lista_personajes)):
            if lista_personajes[i][propiedad] >  lista_personajes[indice][propiedad]:
                indice = i
    else:
        return -1
    return indice

def calcular_min(lista_personajes:list, propiedad:str):
    indice = 0
    if len(lista_personajes) > 0:
        for i in range(len(lista_personajes)):
            if lista_personajes[i][propiedad] < lista_personajes[indice][propiedad]:
                indice = i
    else:
        return -1
    return indice

def calcular_max_min_dato(lista_personajes, propiedad, max = True):
    if max:
        indice = calcular_max(lista_personajes, propiedad)
    else:
        indice = calcular_min(lista_personajes, propiedad)
    return indice
'''
5.1. Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una
lista de héroes y un string que representara el dato/key de los héroes que se
requiere sumar. Validar que cada héroe sea tipo diccionario y que no sea un
diccionario vacío antes de hacer la suma. La función deberá retorna la suma
de todos los datos según la key pasada por parámetro
'''
def sumar_dato_heroe(lista_personajes:list, propiesdad:str):
    suma = 0
    if len(lista_personajes) > 0:
        for i in lista_personajes:
            suma += i[propiesdad]
    return suma

def dividir(dividendo, divisor):
    if divisor == 0:
        return 0
    else:
        resultado = dividendo / divisor
        return resultado

'''
5.3. Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una
lista de héroes y un string que representa el dato del héroe que se requiere
calcular el promedio. La función debe retornar el promedio del dato pasado
por parámetro
'''
def calcular_promedio(lista_personajes:list, propiesdad:str):
    suma = sumar_dato_heroe(lista_personajes, propiesdad)
    promedio = dividir(suma, len(lista_personajes))
    return promedio


while True:
    print(menu)
    option = int(input('Seleccione una opción '))

    match(option):
        case 1:
            imprimir(lista_personajes, 'nombre')
        case 2:
            propiedad = input('Escriba la propiedad que quiera ver ')
            imprimir(lista_personajes, propiedad)
        case 3:
            nombre = input('Escriba el nombre ')
            propiedad = input('Escriba la propiedad ')
            nombre_propiedad = obtener_nombre_y_dato(lista_personajes, nombre, propiedad)
            print(nombre_propiedad)
        case 4:
            print(stark_imprimir_nombres_alturas(lista_personajes))
        case 5:
            propiedad= input('que propiedad quiere calcular ')
            maximo_minimo = input('Quiere calcular el maximo o minimo ')
            if maximo_minimo == 'maximo':
                max = True
                calculo = 'maximo'
            else:
                max = False
                calculo = 'mínimo'

            indice = calcular_max_min_dato(lista_personajes, propiedad, max = True)
            print(f"El heroe con {calculo} {propiedad} es {lista_personajes[indice]['nombre']} con {lista_personajes[indice][propiedad]}")
        case 6:
            propiesdad = input('Escriba la propiedad a sacar el promedio ')
            promedio = round(calcular_promedio(lista_personajes, propiesdad), 2)

            print(f"el promedio del atributo {propiesdad} es {promedio}")