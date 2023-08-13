#burbujeo
def ivan_sort_B(lista_original:list,flag_orden:bool):
    lista = lista_original[:]
    rango_a = len(lista) - 1
    flag_swap = True

    while(flag_swap):
        flag_swap = False

        for indice_A in range(rango_a):
            if  flag_orden == False and lista[indice_A] < lista[indice_A+1] \
             or flag_orden == True and lista[indice_A] > lista[indice_A+1]:
                lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                flag_swap = True
    return lista

#quick sort
def quick_sort(lista_original:list,flag_orden:bool)->list:
    lista_de = []
    lista_iz = []
    if(len(lista_original)<=1):
        return lista_original
    else:
        pivot = lista_original[0]
        for elemento in lista_original[1:]:
            if(elemento > pivot):
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)
    lista_iz = quick_sort(lista_iz,True)
    lista_iz.append(pivot)
    lista_de = quick_sort(lista_de,True)
    lista_iz.extend(lista_de)
    return lista_iz


def ordenar_y_listar_por_clave(lista_original: list, clave: str) -> list:
    '''
    Ordena una lista de jugadores por una clave específica y devuelve la lista ordenada.

    La función utiliza el algoritmo de ordenamiento rápido (quicksort) para ordenar la lista
    de jugadores en base al valor de la clave especificada. Retorna la lista ordenada.

    Args:
        lista_original (list): La lista original de jugadores.
        clave (str): La clave por la cual se va a realizar el ordenamiento.

    Returns:
        lista_ordenada (list): La lista ordenada de jugadores.
    '''
    lista_de = []
    lista_iz = []

    if (len(lista_original) <= 1):
        return lista_original
    else:
        pivot = lista_original[0]["estadisticas"][clave]
        for jugador in lista_original[1:]:
            if (jugador["estadisticas"][clave] < pivot):
                lista_de.append(jugador)
            else:
                lista_iz.append(jugador)

    lista_iz = ordenar_y_listar_por_clave(lista_iz, clave)
    lista_iz.append(lista_original[0])
    lista_de = ordenar_y_listar_por_clave(lista_de, clave)
    lista_iz.extend(lista_de)
    return lista_iz



def ordenar_heroes(lista_original: list, clave: str) -> list:

    lista_de = []
    lista_iz = []

    if (len(lista_original) <= 1):
        return lista_original
    else:
        pivot = lista_original[0][clave]
        for jugador in lista_original[1:]:
            if (jugador[clave] < pivot):
                lista_de.append(jugador)
            else:
                lista_iz.append(jugador)

    lista_iz = ordenar_y_listar_por_clave(lista_iz, clave)
    lista_iz.append(lista_original[0])
    lista_de = ordenar_y_listar_por_clave(lista_de, clave)
    lista_iz.extend(lista_de)
    return lista_iz