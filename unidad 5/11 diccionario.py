'''

Crea un diccionario que represente una lista de tareas por hacer.
Cada clave del diccionario debe ser el nombre de una tarea y cada valor debe ser su estado (los estados son:
pendiente, en proceso, completada). Imprimir todas las tareas seguido de su estado

'''

tarea= {'Matematica': 'pendiente', 'python': 'proceso', 'SDP': 'completada'}

for clave, valor in tarea.items():
    print(f'{clave} : {valor}')