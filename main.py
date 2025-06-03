from Menu import Menu
from Gestores import GestorPacientes
from Gestores import GestorMedicos

class Main:
    def __init__(self):
        self.menu_principal = Menu(["Gestión de pacientes", "Gestión de medicos", "Salir"])
        self.gestor_pacientes = GestorPacientes("pacientes.bin")
        self.gestor_medicos = GestorMedicos("medicos.bin")

    
    def _submenuGestionPacientes(self):
        submenu_pacientes = Menu(["Listar todos", "Buscar por DNI", "Agregar nuevo paciente", "Modificar (nombre, fecha de nacimiento, obra social)", "Eliminar registro", "Guardar cambios", "Volver al menú principal"])

        while True:
            submenu_pacientes.mostrarMenu("gestión pacientes")

            submenu_pacientes_opcion_seleccionada = submenu_pacientes.pedirOpcionDeMenuValida()
            if submenu_pacientes_opcion_seleccionada == 1:
                self.gestor_pacientes.listarPacientes()
            if submenu_pacientes_opcion_seleccionada == 2:
                self.gestor_pacientes.buscarPacientePorDni()
            if submenu_pacientes_opcion_seleccionada == 3:
                self.gestor_pacientes.agregarPaciente()
            if submenu_pacientes_opcion_seleccionada == 4:
                self.gestor_pacientes.modificarPaciente()
            if submenu_pacientes_opcion_seleccionada == 5:
                self.gestor_pacientes.eliminarPaciente()
            if submenu_pacientes_opcion_seleccionada == 6:
                self.gestor_pacientes._guardarListaPacientes()
            elif submenu_pacientes_opcion_seleccionada == 7:
                break


    def _submenuGestionMedicos(self):
        submenu_medicos = Menu(["Listar todos", "Buscar por matricula", "Agregar nuevo medico", "Modificar (nombre, especialidad)", "Eliminar registro", "Guardar cambios", "Volver al menú principal"])

        while True:
            submenu_medicos.mostrarMenu("gestión medicos")

            submenu_medicos_opcion_seleccionada = submenu_medicos.pedirOpcionDeMenuValida()
            if submenu_medicos_opcion_seleccionada == 1:
                self.gestor_medicos.listarMedicos()
            elif submenu_medicos_opcion_seleccionada == 2:
                self.gestor_medicos.buscarMedicoPorMatricula()
            elif submenu_medicos_opcion_seleccionada == 3:
                self.gestor_medicos.agregarMedico()
            elif submenu_medicos_opcion_seleccionada == 4:
                self.gestor_medicos.modificarMedico()
            elif submenu_medicos_opcion_seleccionada == 5:
                self.gestor_medicos.eliminarMedico()
            elif submenu_medicos_opcion_seleccionada == 6:
                self.gestor_medicos._guardarListaMedicos()
            elif submenu_medicos_opcion_seleccionada == 7:
                break


    
    def ejecutar(self):
        while True:
            self.menu_principal.mostrarMenu()
            menu_principal_opcion_seleccionada = self.menu_principal.pedirOpcionDeMenuValida()

            if menu_principal_opcion_seleccionada == 1:
                self._submenuGestionPacientes()
            elif menu_principal_opcion_seleccionada == 2:
                self._submenuGestionMedicos()
            elif menu_principal_opcion_seleccionada == 3:
                print("\n Hasta luego!")
                break
            
            input("\nPresione Enter para continuar. ")

main = Main()
main.ejecutar()