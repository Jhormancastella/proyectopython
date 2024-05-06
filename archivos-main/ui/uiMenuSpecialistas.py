import modules.corefiles as cf
import funciones.globales as gf
import funciones.especialistas as fsp
import funciones.iraconsulta as fic
import main

def MenuEspecialista(op: int):
    title = """
    ➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖
   ⚕️  🧑‍⚕️  MODULO ADMIN ESPECIALISTAS CENTRO CLINICO  👩‍⚕️  ⚕️
    ➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖➖〰️➖⚕️➖〰️➖
    """
    menuEspecialistaOp = '1. Agregar\n2. Editar\n3. ir a consulta\n4. eliminar\n5. Salir'
    gf.borrar_pantalla()
    if op != 5:  # Reemplazado 4 con 5 para salir en la opción 5
        print(title)
        print(menuEspecialistaOp)
        while True:
            try:
                op = int(input(":) "))
                if op not in range(1, 6):
                    raise ValueError("La opción ingresada no está en el rango válido")
                break
            except ValueError as e:
                print("Error:", e)
                gf.pausar_pantalla()
                MenuEspecialista(0)

        match op:
            case 1:
                try:
                    fsp.NewEspecialista()
                except Exception as e:
                    print("Error al agregar especialista:", e)
                else:
                    print("Especialista agregado exitosamente")
                gf.pausar_pantalla()
                MenuEspecialista(0)

            case 2:
                try:
                    fsp.ModifyData()
                except Exception as e:
                    print("Error al editar especialista:", e)
                else:
                    print("Datos del especialista editados exitosamente")
                gf.pausar_pantalla()
                MenuEspecialista(0)

            case 3:
                try:
                    fic.iraConsulta()
                except Exception as e:
                    print("Error al ir a consulta:", e)
                gf.pausar_pantalla()
                MenuEspecialista(0)

            case 4:
                try:
                    fsp.DeleteData()
                except Exception as e:
                    print("Error al eliminar especialista:", e)
                else:
                    print("Especialista eliminado exitosamente")
                gf.pausar_pantalla()
                MenuEspecialista(0)

            case 5:
                main.mainMenu(0)

            case _:
                print("La opción ingresada no está disponible en las opciones")
                gf.pausar_pantalla()
                MenuEspecialista(0)
