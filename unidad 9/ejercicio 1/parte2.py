#2.1 evaluar si es M o F
def es_genero(lista_heroes:dict, nombre:str, genero:str):
    for i in lista_heroes:
        if i['nombre'] == nombre:
            if i['genero'] == genero:
                return True
            else:
                return False

# 2.2 guardar por genero
def lista_genero_func(lista_heroes:dict, genero:str):
    cadena_nombre_genero = ""
    for i in lista_heroes:
        if i['genero'] == genero:
            cadena_nombre_genero += i['nombre'] + " "
    return cadena_nombre_genero


    '''
    with open(nombre_archivo, 'w') as archivo:
        for video in lista:
            texto_linea = f"{video['video].replace(', ',' - '}.replace('\n', ' @ ')
            , {video['views']}, {video['title']}}
            archivo.writtetexto_linea)
    '''