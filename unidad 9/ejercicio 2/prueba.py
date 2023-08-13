

def quick_sort(lista_original:list,flag_orden:bool)->list:
    lista_de = []
    lista_iz = []
    if(len(lista_original)<=1):
        return lista_original
    else:
        pivot = lista_original[0]
        for elemento in lista_original[1:]:
            if flag_orden:
                if(elemento > pivot):
                    lista_de.append(elemento)
                else:
                    lista_iz.append(elemento)
            else:
                if (elemento < pivot):
                    lista_de.append(elemento)
                else:
                    lista_iz.append(elemento)
    lista_iz = quick_sort(lista_iz,flag_orden)
    lista_iz.append(pivot)
    lista_de = quick_sort(lista_de,flag_orden)
    lista_iz.extend(lista_de)
    return lista_iz

lista = [10,15,20,68,45,10,2,987,124,4]
lista2 = ['Hola', 'q', 'tal', 'z', 'a']

print(quick_sort(lista2, True))


import json
def abrir_json(ruta:str) -> json:
    with open(ruta) as f:
        lista_heroes = json.load(f)
        return lista_heroes['jugadores']

basquebolistas = abrir_json('dt.json')

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

print(ordenar_y_listar_por_clave(basquebolistas, "promedio_puntos_por_partido"))