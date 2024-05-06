import modules.corefiles as cf
import funciones.globales as gf
import funciones.Paciente as pt
import main

def MenuPacientes(op: int):
    title = """
    🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥
    🕛 MODULO ADMIN PACIENTES CENTRO CLINICO  🕛
    🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥
    """
    menuPacienteOp = '1. Agregar\n2. Editar\n3. Eliminar\n4. Salir'
    gf.borrar_pantalla()
    if op != 4:
        print(title)
        print(menuPacienteOp)
        while True:
            try:
                op = int(input(":) "))
                if op not in range(1, 5):
                    raise ValueError("La opción ingresada no está en el rango válido")
                break
            except ValueError as e:
                print("Error:", e)
                gf.pausar_pantalla()
                MenuPacientes(0)

        match op:
            case 1:
                try:
                    pt.NewPaciente()
                except Exception as e:
                    print("Error al agregar paciente:", e)
                else:
                    print("Paciente agregado exitosamente")
                gf.pausar_pantalla()
                MenuPacientes(0)

            case 2:
                try:
                    pt.ModifyData()
                except Exception as e:
                    print("Error al editar paciente:", e)
                else:
                    print("Datos del paciente editados exitosamente")
                gf.pausar_pantalla()
                MenuPacientes(0)

            case 3:
                try:
                    pt.DeleteData()
                except Exception as e:
                    print("Error al eliminar paciente:", e)
                else:
                    print("Paciente eliminado exitosamente")
                gf.pausar_pantalla()
                MenuPacientes(0)

            case 4:
                main.mainMenu(0)

            case _:
                print("La opción ingresada no está disponible en las opciones")
                gf.pausar_pantalla()
                MenuPacientes(0)
