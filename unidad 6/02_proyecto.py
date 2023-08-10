'''
https://docs.google.com/document/d/1XaB_rNu8gqMp8OuYm4krf9CXSVoYGPJQjhiQbwrzmmM/edit
'''

lista_miembros=[{'id':'1', 'nombre': 'rod', 'edad': 15, 'membresia': 'anual'},
                {'id':'2', 'nombre': 'Pulgas', 'edad': 20, 'membresia': 'mensual'},
                {'id':'3', 'nombre': 'Pimby', 'edad': 25, 'membresia': 'Anual'},
                {'id':'4', 'nombre': 'Ruth', 'edad': 30, 'membresia': 'mensual'},
                {'id':'5', 'nombre': 'Carmen', 'edad': 50, 'membresia': 'Anual'}]

menu = '''
    1 agregar
    2 Mostrar toda la información
    3 Actualizar el tipo de membresía de un miembro
    4 Buscar información de un miembro
    5 Calcular el promedio de edad de los miembros
    6 Buscar el miembro más joven y el más viejo
    '''
'''
1. Agregar un nuevo miembro: el programa debe pedir al usuario que ingrese el
número de identificación, nombre, edad y tipo de membresía del nuevo
miembro. La información debe ser agregada a la lista de diccionarios.
'''
def agregar(si=True):
    while si:
        agregar_dict={}

        id = int(input('escriba el id '))
        nombre = input('escriba un nombre ')
        edad = int(input('Edad '))
        membresia = input('membresia ')

        agregar_dict['id'] = id
        agregar_dict['nombre'] = nombre
        agregar_dict['edad'] = edad
        agregar_dict['membresia'] = membresia

        lista_miembros.append(agregar_dict)

        opcion = input('Seguir agregando s - n')

        if opcion == 's':
            si = True
        else:
            si = False


'''
2. Mostrar toda la información de todos los miembros (número de identificación,
nombre, edad y tipo de membresía).
'''
def mostrar():
    for i in range(len(lista_miembros)):
        print(f" id: {lista_miembros[i]['id']} - Nombre: {lista_miembros[i]['nombre']} "
              f"- Edad: {lista_miembros[i]['edad']} - Membresia: {lista_miembros[i]['membresia']} ")

'''
3. Actualizar el tipo de membresía de un miembro: el programa debe pedir al
usuario que ingrese el número de identificación del miembro y el nuevo tipo
de membresía. El programa debe buscar el miembro en la lista de diccionario
y actualizar el tipo de membresía correspondiente.
'''
def actualizar(idCambiar, membresiaCambiar ):
    for i in lista_miembros:
        if i['id']== idCambiar:
            i['membresia'] = membresiaCambiar

'''
4. Buscar información de un miembro: el programa debe pedir al usuario que
ingrese el número de identificación del miembro. El programa debe buscar el
miembro en la lista de diccionarios y mostrar su nombre, edad y tipo de
membresía.
'''
def buscar(idBuscar):
    for i in lista_miembros:
        if i['id'] == idBuscar:
            print(f" Nombre: {i['nombre']} "
                  f"- Edad: {i['edad']} - Membresia: {i['membresia']} ")

'''
5. Calcular el promedio de edad de los miembros: el programa debe recorrer la
lista de diccionarios y calcular el promedio de edad de los miembros.
'''

def promedio(lista_miembros):
    suma = 0
    for i in lista_miembros:
        suma += i['edad']

    promedio = suma / len(lista_miembros)
    return promedio
'''
6. Buscar el miembro más joven y el más viejo: el programa debe buscar la edad
máxima y mínima en la lista de diccionarios y mostrar el nombre y número de
identificación correspondientes.
'''
def mas_viejo_joven(lista_miembros):
    indice_viejo=0
    indice_joven = 0
    for i in range(len(lista_miembros)):
        if lista_miembros[indice_viejo]['edad'] > lista_miembros[i]['edad']:
            indice_viejo = i
        elif lista_miembros[indice_joven]['edad'] < lista_miembros[i]['edad']:
            indice_joven = i

    print(f" El más joven tiene el id: {lista_miembros[indice_joven]['id']} - y el  Nombre: {lista_miembros[indice_joven]['nombre']}")
    print(f" El más viejo tiene el id: {lista_miembros[indice_viejo]['id']} - y el  Nombre: {lista_miembros[indice_viejo]['nombre']}")

while True:
    print(menu)

    opcion = int(input('Eliga una opción '))

    match(opcion):
        case 1:
            agregar()
        case 2:
            mostrar()
        case 3:
            idCambiar = input('Ingrese el ID')
            membresiaCambiar = input('Ingrese la membresía actual ')
            actualizar(idCambiar, membresiaCambiar)
        case 4:
            idBuscar = input('Ingrese el ID')
            buscar(idBuscar)
        case 5:
            print(f"el promedio de edad es {promedio(lista_miembros)}")
        case 6:
            mas_viejo_joven(lista_miembros)
        case 7:
            break
