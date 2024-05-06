import modules.corefiles as cf
import modules.corefilesP as cfp
import funciones.globales as fg
import ui.uiMenuSpecialistas as uiSp
import ui.uiMenuPacientes as uiPt
import ui.uiConsultas as uiC

def mainMenu(op):
    fg.borrar_pantalla()
    title = """
    🟦⬜🟦🟩⬜🟩🟦⬜🟦🟩⬜🟩🟦⬜🟦🟩⬜🟩🟦⬜🟦🟩⬜🟩
    🟥 🏣🚑👨‍⚕️👩‍⚕️🏥 CENTRO CLINICO 🏣🚑👨‍⚕️👩‍⚕️🏥  🟥
    🟦⬜🟦🟩⬜🟩🟦⬜🟦🟩⬜🟩🟦⬜🟦🟩⬜🟩🟦⬜🟦🟩⬜🟩
    """
    mainMenuOp = "1. Gestion especialistas\n2. Gestion pacientes\n3. agendar Consulta y resultados\n4. Salir"
    if op != 4:
        print(title)
        print(mainMenuOp)
        try:
            opcion = int(input(':) '))
        except ValueError:
            print('Error en la opcion ingresada')
            fg.pausar_pantalla()
            mainMenu(0)
        else:
            if opcion == 1:
                uiSp.MenuEspecialista(0)
            elif opcion == 2:
                uiPt.MenuPacientes(0)
            elif opcion == 3:
                uiC.MenuConsulta(0)
            elif opcion == 4:
                print("Regrese pronto ....")
                fg.pausar_pantalla()
            else:
                print('Opcion ingresada no pertenece al menu de opciones')
                fg.pausar_pantalla()
                mainMenu(0)

if __name__ == '__main__':
    cf.MY_DATABASE = 'data/pacientes.json'
    cfp.MY_DATABASEP = 'data/especialistas.json'
    cf.checkFile(fg.centroClinico)
    cfp.checkFile(fg.centroClinico)
    mainMenu(0)
