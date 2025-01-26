"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_09():
    with open('files/input/data.csv', 'r') as file:
        data = list(csv.reader(file, delimiter='\t'))
        
    data = [row[4] for row in data]

    data = [row.split(',') for row in data]

    data = [dict([row.split(':') for row in row]) for row in data]
    keys = set([key for row in data for key in row.keys()])

    result = []
    for key in keys:
        values = [int(row[key]) for row in data if key in row]
        result.append((key, len(values)))
    
    result = sorted(result, key=lambda x: x[0])
    result = dict(result)
    return result
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

