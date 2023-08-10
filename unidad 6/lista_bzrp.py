'''
https://docs.google.com/document/d/1XaB_rNu8gqMp8OuYm4krf9CXSVoYGPJQjhiQbwrzmmM/edit
'''

miembro_id = ['1', '2', '3', '4', '5']
miembro_nombre = ['rod', 'carmen', 'Guillermo', 'pimby', 'maca']
miembro_edad = [10, 20, 30, 40, 50]
miembro_membresia = ['mensual', 'anual', 'mensual', 'anual', 'mensual']


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
        id= input('Id ')
        nombre = input('Nombre ')
        edad = input('Edad ')
        edad = int(edad)
        tipo_membresía = input('Tipo de membresía ')

        miembro_id.append(id)
        miembro_nombre.append(nombre)
        miembro_edad.append(edad)
        miembro_membresia.append(tipo_membresía)

    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        print("Nro ID.\tNombre\tEdad\tTipo membresia")

        for i in range(len(miembro_id)):
            print(f'Id {miembro_id[1]} - Nombre: {miembro_nombre[i]} - Edad: {miembro_edad[i]} - Tipo de membresía: {miembro_membresia[i]} ')

    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        id_membresia = input('Indique el ID que quiere actualizar')
        encontrado = False
        for i in range(len(miembro_id)):
            if miembro_id[i] == id_membresia:
                encontrado=True
                cambio_membresia = input('Escriba el cambio de membresia ')
                miembro_membresia[i] = cambio_membresia
                break
        if encontrado == False:
            print('No se econtró el Id')


    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        encontrado = False
        id = input('Indique el ID ')
        for i in range(len(miembro_id)):
            encontrado = True
            if miembro_id[i] == id:
                print(f'Id {miembro_id[1]} - Nombre: {miembro_nombre[i]} - Edad: {miembro_edad[i]} - Tipo de membresía: {miembro_membresia[i]} ')
                break
        if encontrado == False:
            print('No se econtró el Id')


    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        suma=0
        cant=0
        for i in range(len(miembro_edad)):
            suma+= miembro_edad[i]
            cant+=1

        promedio = suma / cant
        print(f'El promedio es {promedio}')


    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        flag= False

        for i in range(len(miembro_edad)):
            if flag == False:
                flag= True
                menor = miembro_edad[i]
                nombreJoven = miembro_nombre[i]
                idJoven= miembro_id[i]

                mayor = miembro_edad[i]
                nombreViejo = miembro_nombre[i]
                idViejo = miembro_id[i]

            elif menor > miembro_edad[i]:
                menor = miembro_edad[i]
                nombreJoven = miembro_nombre[i]
                idJoven = miembro_id[i]

            elif mayor < miembro_edad[i]:
                mayor = miembro_edad[i]
                nombreViejo = miembro_nombre[i]
                idViejo = miembro_id[i]
        print(f'El miembro con la edad menor de {nombreJoven} con Id: {idJoven}  ')
        print(f'El miembro con la edad Mayor de {nombreViejo} con Id: {idViejo}  ')


    # Opcion 0: Salir
    elif opcion == "0":
        break


    else:
        print("Opción inválida. Intente de nuevo.")

for i in range(len(list)):
    if mayor_num < num:
 break