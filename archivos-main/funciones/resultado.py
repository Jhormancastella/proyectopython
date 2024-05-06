import json

def imprimir_tratamiento(identificacion):
    try:
        with open("historial.json", "r") as file:
            historial = json.load(file)
            tratamiento = historial.get(identificacion)
            if tratamiento:
                print("Tratamiento del paciente:", tratamiento)
            else:
                print("No se encontró tratamiento para este paciente en el historial.")
    except FileNotFoundError:
        print("El archivo historial.json no fue encontrado.")
    except json.JSONDecodeError:
        print("El archivo historial.json no tiene un formato JSON válido.")
    except Exception as e:
        print("Se produjo un error:", e)
