from data_bzrp import lista_bzrp


#casteamos los datos
for i in lista_bzrp:
    i['views'] = int(i['views'])
    i['length'] = int(i['length'])


def tema_mas_menos_visto_largo(atributo, mas=True):
    indice = 0
    if mas == True:
        for i in range(len(lista_bzrp)):
            if lista_bzrp[i][atributo] > lista_bzrp[indice][atributo]:
                indice = i
    else:
        for i in range(len(lista_bzrp)):
            if lista_bzrp[i][atributo] < lista_bzrp[indice][atributo]:
                indice = i

    return indice

def promedio (atributo):
    suma = 0
    for i in range(len(lista_bzrp)):
        suma += lista_bzrp[i][atributo]

    promedio = suma / len(lista_bzrp)
    return promedio


menu ='''
    1 - Tema mas visto
    2 - Tema menos visto
    3 - Tema mas largo
    4 - Tema mas corto
    5 - Duracion promedio de temas
    6 - Promedio de vistas 
    7 - Salir
    '''

while True:
    print(menu)
    option = int(input('Eleija una opción '))

    match(option):
        case 1:
            indice = tema_mas_menos_visto_largo('views', mas=True)
            print(f"el nombre de tema con más vistas {lista_bzrp[indice]['title']} con {lista_bzrp[indice]['views']} views")

        case 2:
            indice = tema_mas_menos_visto_largo('views', mas=False)
            print(f"el nombre de tema con menos vistas {lista_bzrp[indice]['title']} con {lista_bzrp[indice]['views']} views")

        case 3:
            indice = tema_mas_menos_visto_largo('length', mas=True)
            print(f"el nombre de tema con más vistas {lista_bzrp[indice]['title']} con {lista_bzrp[indice]['length']} de largo")

        case 4:
            indice = tema_mas_menos_visto_largo('length', mas=False)
            print(f"el nombre de tema con más vistas {lista_bzrp[indice]['title']} con {lista_bzrp[indice]['length']} de largo")

        case 5:
            print(f"El promedio de temas es {round(promedio('length'), 2)}")

        case 6:
            print(f"El promedio de vistas es {round(promedio('views'), 2)}")

        case 7:
            break
