'''
https://docs.google.com/document/d/1XaB_rNu8gqMp8OuYm4krf9CXSVoYGPJQjhiQbwrzmmM/edit
'''

lista_miembros=[{'id':'1', 'nombre': 'rod', 'edad': 15, 'membresia': 'anual'},
                {'id':'2', 'nombre': 'Pulgas', 'edad': 20, 'membresia': 'mensual'},
                {'id':'3', 'nombre': 'Pimby', 'edad': 25, 'membresia': 'Anual'},
                {'id':'4', 'nombre': 'Ruth', 'edad': 30, 'membresia': 'mensual'},
                {'id':'5', 'nombre': 'Carmen', 'edad': 50, 'membresia': 'Anual'}]

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")


    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":

        diccionario_miembros={}

        id= input('Ingrese Id ')
        nombre = input('Ingrese Nombre ')
        edad = input ('ingrese edad ')
        edad= int(edad)
        membresia = input('Ingrese tipo de membresia')

        diccionario_miembros['id'] = id
        diccionario_miembros['nombre'] = nombre
        diccionario_miembros['edad'] = edad
        diccionario_miembros['membresia'] = membresia

        lista_miembros.append(diccionario_miembros)


        # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        print("Nro ID.\tNombre\tEdad\tTipo membresia")

        for i in lista_miembros:
            for k, v in i.items():
                print(k, v)


    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        id_membresia = input('Indique el ID que quiere actualizar ')
        encontrado = False

        #lista_diccionario[indice][clave]

        for i in range(len(lista_miembros)):
            if id_membresia == lista_miembros[i]['id']:
                encontrado = True
                cambio_membresia = input('Escriba el cambio de membresia ')
                lista_miembros[i]['membresia'] = cambio_membresia
                break

        if encontrado == False:
            print('No se econtró el Id')

    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        id_membresia = input('Indique el ID que quiere buscar ')
        encontrado = False

        for i in range(len(lista_miembros)):
            if id_membresia == lista_miembros[i]['id']:
                encontrado=True
                print(f' Id: {lista_miembros[i]["id"]} - Nombre: {lista_miembros[i]["nombre"]} - edad: {lista_miembros[i]["edad"]} - Membresia: {lista_miembros[i]["membresia"]}')
                break

    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        suma=0
        cant=0
        for i in range(len(lista_miembros)):
            suma+= lista_miembros[i]['edad']
            cant+=1

        promedio= suma/cant
        print(f'El promedio es {promedio}')



    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        flag = False

        for i in range(len(lista_miembros)):
            if flag == False:
                flag = True
                menor = lista_miembros[i]['edad']
                nombreJoven = lista_miembros[i]['nombre']
                idJoven = lista_miembros[i]['id']

                mayor = lista_miembros[i]['edad']
                nombreViejo = lista_miembros[i]['nombre']
                idViejo = lista_miembros[i]['id']

            elif menor > lista_miembros[i]['edad']:
                menor = lista_miembros[i]
                nombreJoven = lista_miembros[i]['nombre']
                idJoven = lista_miembros[i]['id']

            elif mayor < lista_miembros[i]['edad']:
                mayor = lista_miembros[i]['edad']
                nombreViejo = lista_miembros[i]['nombre']
                idViejo = lista_miembros[i]['id']
        print(f'El miembro con la edad menor de {nombreJoven} con Id: {idJoven}  ')
        print(f'El miembro con la edad Mayor de {nombreViejo} con Id: {idViejo}  ')


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")


