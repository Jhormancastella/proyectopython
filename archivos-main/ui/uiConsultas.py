import modules.corefiles as cf
import funciones.globales as gf
import funciones.ConsultarResultados as pt
import funciones.resultado as frt
import main

def MenuConsulta(op: int):
    title = """
    *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣  
    *️⃣ *️⃣    MODULO ADMIN CONSULTA Y RESULTADOS CENTRO CLINICO  *️⃣ *️⃣
    *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ *️⃣ 
    """
    MenuConsultaOp = '1. Agendar Cita\n2. Ver Resultados\n3. Salir'
    gf.borrar_pantalla()
    if op != 3:
        print(title)
        print(MenuConsultaOp)
        while True:
            try:
                op = int(input(":) "))
                if op not in range(1, 4):
                    raise ValueError("La opción ingresada no está en el rango válido")
                break
            except ValueError as e:
                print("Error:", e)
                gf.pausar_pantalla()
                MenuConsulta(0)

        match op:
            case 1:
                try:
                    pt.NewConsulta()
                except Exception as e:
                    print("Error al agendar cita:", e)
                else:
                    print("Cita agendada exitosamente")
                gf.pausar_pantalla()
                MenuConsulta(0)

            case 2:
                try:
                    frt.imprimir_tratamiento()
                except Exception as e:
                    print("Error al ver resultados:", e)
                gf.pausar_pantalla()
                MenuConsulta(0)

            case 3:
                main.mainMenu(0)

            case _:
                print("La opción ingresada no está disponible en las opciones")
                gf.pausar_pantalla()
                MenuConsulta(0)
