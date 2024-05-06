import os
import json
import funciones.globales as gf
from datetime import datetime, timedelta
import ui.uiConsultas as uc

def SearchData():
    criterio = input('Ingrese el Nro de Identificacion del paciente: ')
    data = gf.centroClinico.get('data').get(criterio)
    return data

def NewConsulta():
    title = """
    ***************************
    * REGISTRO DE CONSULTA *
    ***************************
    """
    gf.borrar_pantalla()
    print(title)

    # Ruta al archivo pacientes.json dentro de la carpeta "data"
    pacientes_file = os.path.join("data", "pacientes.json")

    # Verificar si el archivo pacientes.json existe
    if not os.path.exists(pacientes_file):
        print("El archivo pacientes.json no se encuentra en la carpeta 'data'. Por favor, asegúrese de que el archivo esté presente.")
        return

    while True:
        paciente = SearchData()
        if paciente:
            fecha_registro = datetime.now().strftime("%Y-%m-%d")  # Fecha de registro
            print(f"Fecha de registro de la consulta: {fecha_registro}")

            motivo = input("Ingrese el motivo de la consulta: ")
            antecedentes = input("Ingrese los antecedentes del paciente: ")
            alergias = input("Ingrese las alergias del paciente: ")
            
            print("Seleccione el especialista:")
            print("1. Pediatría")
            print("2. Ginecología")
            print("3. Dermatología")
            print("4. Endocrinología")
            print("5. Optometría")
            especialista = input("Ingrese el número correspondiente al especialista: ")
            
            horario_inicio = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)  # Horario inicio
            if input("¿Prefiere la cita por la mañana? (Sí/No): ").lower() == 'sí':
                horario_inicio = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
            else:
                horario_inicio = datetime.now().replace(hour=14, minute=0, second=0, microsecond=0)
            
            # Calcular fecha de la cita (2 días después de la fecha de registro)
            fecha_cita = datetime.now() + timedelta(days=2)
            fecha_cita_str = fecha_cita.strftime("%Y-%m-%d")

            # Calcular horario de la cita (20 minutos por consulta)
            horario_fin = horario_inicio + timedelta(minutes=20)
            horario_str = f"{horario_inicio.strftime('%I:%M %p')} - {horario_fin.strftime('%I:%M %p')}"

            consultorio = ""
            if especialista == '1':
                consultorio = "Consultorio 101"
            elif especialista == '2':
                consultorio = "Consultorio 201"
            elif especialista == '3':
                consultorio = "Consultorio 301"
            elif especialista == '4':
                consultorio = "Consultorio 401"
            elif especialista == '5':
                consultorio = "Consultorio 501"
            else:
                print("Especialista no válido.")
            
            if consultorio:
                print(f"Su cita ha sido programada con el especialista en {consultorio} para el {fecha_cita_str} a las {horario_str}.")
                print("Por favor, asegúrese de llegar al consultorio 20 minutos antes de la cita.")
                
                # Guardar los datos de la consulta en el paciente
                paciente['consultas'] = paciente.get('consultas', [])
                paciente['consultas'].append({
                    'fecha_cita': fecha_cita_str,
                    'horario_cita': horario_str,
                    'especialista': especialista,
                    'motivo': motivo,
                    'antecedentes': antecedentes,
                    'alergias': alergias,
                    'consultorio': consultorio
                })

                # Actualizar el archivo pacientes.json con los nuevos datos
                with open(pacientes_file, "w") as file:
                    json.dump(gf.centroClinico, file, indent=4)

                if input("¿Desea agregar otra consulta? (Sí/No): ").lower() != 'sí':
                    break  # Salir del bucle si no se desea agregar otra consulta
            else:
                print("Cita no programada debido a una selección de especialista inválida.")
        else:
            print("Paciente no encontrado.")
            if input("¿Desea volver al menú de consultas? (Sí/No): ").lower() != 'sí':
                break  # Salir del bucle si no se desea agregar otra consulta
            else:
                continue  # Volver al inicio del bucle para ingresar otro número de identificación
