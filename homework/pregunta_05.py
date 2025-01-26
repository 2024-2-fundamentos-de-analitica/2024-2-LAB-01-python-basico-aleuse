"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_05():
    with open('files/input/data.csv', 'r') as file:
        data = list(csv.reader(file, delimiter='\t'))
        
    data = data[1:]
    data = sorted(data, key=lambda x: x[0])
    result = []
    
    for i in range(len(data)):
        if i == 0:
            letter = data[i][0]
            max_value = int(data[i][1])
            min_value = int(data[i][1])
        elif data[i][0] != letter:
            result.append((letter, max_value, min_value))
            letter = data[i][0]
            max_value = int(data[i][1])
            min_value = int(data[i][1])
        else:
            max_value = max(max_value, int(data[i][1]))
            min_value = min(min_value, int(data[i][1]))
    
    result.append((letter, max_value, min_value))
    return result
    
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
