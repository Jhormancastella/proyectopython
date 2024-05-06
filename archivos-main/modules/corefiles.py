import json
import os

MY_DATABASE = 'data/pacientes.json'

def NewFile(data):
    try:
        with open(MY_DATABASE, "w") as wf:
            json.dump(data, wf, indent=4)
    except IOError as e:
        print("Error al crear el archivo:", e)

def UpdateFile(data):
    try:
        with open(MY_DATABASE, 'w') as fw:
            json.dump(data, fw, indent=4)
    except IOError as e:
        print("Error al actualizar el archivo:", e)

def AddData(*param):
    try:
        data = list(param)
        with open(MY_DATABASE, "r+") as rwf:
            data_file = json.load(rwf)
            if len(param) > 1:
                data_file[data[0]].update({data[1]: data[2]})
            else:
                data_file.update({param[0]})
            rwf.seek(0)
            json.dump(data_file, rwf, indent=4)
    except (IOError, json.JSONDecodeError) as e:
        print("Error al añadir datos al archivo:", e)

def ReadFile():
    try:
        with open(MY_DATABASE, "r") as rf:
            return json.load(rf)
    except (IOError, json.JSONDecodeError) as e:
        print("Error al leer el archivo:", e)
        return {}

def checkFile(data=None):
    try:
        if os.path.isfile(MY_DATABASE):
            if data is not None:
                data.update(ReadFile())
        else:
            if data is not None:
                NewFile(data)
    except IOError as e:
        print("Error al verificar el archivo:", e)
