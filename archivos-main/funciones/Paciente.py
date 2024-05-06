import json
import os
import funciones.globales as gf
import modules.corefiles as cf
import ui.uiMenuPacientes as uipc
from datetime import datetime

def NewPaciente():
    title = """
    ***************************
    * REGISTRO DE PACIENTES *
    ***************************
    """
    gf.borrar_pantalla()
    print(title)
    try:
        identificacion = input("Ingrese el Nro de Identificacion: ")
        codPaciente = input("Ingrese Codigo del paciente: ")
        nombrePaciente = input("Ingrese Nombre del paciente: ")
        apellidos = input("Ingrese Apellidos del paciente: ")
        telefono = input("Ingrese Número telefónico: ")
        celular = input("Ingrese Número celular: ")
        fecha_nacimiento = input("Ingrese Fecha de nacimiento (formato dd-mm-yyyy): ")
        fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
        edad = calculate_age(fecha_nacimiento)
        genero = input("Ingrese Género del paciente: ")
        
        paciente = {
            'identificacion': identificacion,
            'codPaciente': codPaciente,
            'nombrePaciente': nombrePaciente,
            'apellidos': apellidos,
            'telefono': telefono,
            'celular': celular,
            'fecha_nacimiento': fecha_nacimiento.strftime("%d-%m-%Y"),
            'edad': edad,
            'genero': genero,
            'consultas': [],
        }
        
        cf.AddData('data', identificacion, paciente)
        gf.centroClinico.get('data').update({identificacion: paciente})
        
        if input('Desea registrar otro paciente (Sí) o Enter (No): ').strip().lower() == 's':
            NewPaciente()
        else:
            uipc.MenuPacientes(0)
            
    except Exception as e:
        print("Error al registrar paciente:", e)

def calculate_age(born):
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def SearchData():
    try:
        criterio = input('Ingrese el Nro de Identificacion del paciente: ')
        data = gf.centroClinico.get('data').get(criterio)
        return data
    except Exception as e:
        print("Error al buscar datos del paciente:", e)
        return None

def ModifyData():
    try:
        dataPaciente = SearchData()
        if dataPaciente:
            identificacion, codPaciente, nombrePaciente, apellidos, telefono, celular, fecha_nacimiento, edad, genero, consultas = dataPaciente.values()
            for key in dataPaciente.keys():
                if key not in ['identificacion', 'consultas']:
                    if input(f'Desea modificar el {key} (sí) o Enter (No): ').strip().lower() == 's':
                        nuevo_valor = input(f'Ingrese el nuevo valor para {key}: ')
                        dataPaciente[key] = nuevo_valor
                        
            gf.centroClinico.get('data').update({identificacion: dataPaciente})
            cf.UpdateFile(gf.centroClinico)
            uipc.MenuPacientes(0)
        else:
            print("Paciente no encontrado.")
    except Exception as e:
        print("Error al modificar datos del paciente:", e)

def DeleteData():
    try:
        identificacion = input('Ingrese el Nro de Identificacion del paciente a eliminar: ')
        if identificacion in gf.centroClinico.get('data'):
            del gf.centroClinico.get('data')[identificacion]
            cf.UpdateFile(gf.centroClinico)
            print("Paciente eliminado correctamente.")
            uipc.MenuPacientes(0)
        else:
            print("El paciente con el número de identificación ingresado no existe en la base de datos.")
            if input('¿Desea intentar con otro número de identificación? (Sí/No): ').strip().lower() == 's':
                DeleteData()
            else:
                uipc.MenuPacientes(0)
    except Exception as e:
        print("Error al eliminar paciente:", e)
