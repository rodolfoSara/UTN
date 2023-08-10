'''
Crear una función que recibe una lista de diccionarios con información de
películas (título, género, director) y devuelve un diccionario con la cantidad de
películas por género.

'''

def cantidad_peliculas_por_genero(listaPeliculas):
    cantidad_genero={}
    for i in range(len(listaPeliculas)):
        if (listaPeliculas[i]['genero']) in cantidad_genero:
            cantidad_genero[listaPeliculas[i]['genero']] += 1
        else:
            cantidad_genero[listaPeliculas[i]['genero']] = 1

    return cantidad_genero



listaPeliculas =[{'titulo': 'La naranja mecánica', 'genero': 'drama',  'director': 'Stanley Kubrick'},
                 {'titulo': 'Amélie', 'genero': 'Comedia',  'director': 'Jean-Pierre Jeunet'},
                 {'titulo': 'La naranja mecánica', 'genero': 'drama', 'director': 'Stanley Kubrick'},
                 {'titulo': 'Amélie', 'genero': 'Comedia', 'director': 'Jean-Pierre Jeunet'},
                 {'titulo': 'La naranja mecánica', 'genero': 'drama',  'director': 'Stanley Kubrick'}]

cantidadPelisPorGenero = cantidad_peliculas_por_genero(listaPeliculas)
print(cantidadPelisPorGenero)