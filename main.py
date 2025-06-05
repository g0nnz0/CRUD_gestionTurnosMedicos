from Menu import Menu
from Gestores import GestorPacientes
from Gestores import GestorMedicos
from Gestores import GestorTurnos

class Main:
    def __init__(self):
        self.menu_principal = Menu(["Gestión de pacientes", "Gestión de medicos", "Gestión de turnos", "Salir"])
        self.gestor_pacientes = GestorPacientes("pacientes.bin")
        self.gestor_medicos = GestorMedicos("medicos.bin")
        self.gestor_turnos = GestorTurnos("turnos.bin", self.gestor_pacientes, self.gestor_medicos)

    
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

    def _submenuGestionTurnos(self):
        submenu_turnos = Menu(["Listar turnos", "Buscar turno por fecha", "Agregar turno", "Eliminar turno", "Guardar cambios", "Volver al menu principal"])

        while True:
            submenu_turnos.mostrarMenu("gestión turnos")

            submenu_turnos_opcion_seleccionada = submenu_turnos.pedirOpcionDeMenuValida()
            if submenu_turnos_opcion_seleccionada == 1:
                self._submenuGestionTurnos_listados_por_filtro()
            elif submenu_turnos_opcion_seleccionada == 2:
                self.gestor_turnos.buscarTurnoPorFecha()
            elif submenu_turnos_opcion_seleccionada == 3:
                self.gestor_turnos.agregarTurno()
            elif submenu_turnos_opcion_seleccionada == 4:
                self.gestor_turnos.eliminarTurno()
            elif submenu_turnos_opcion_seleccionada == 5:
                self.gestor_turnos._guardarListaTurnos()
            elif submenu_turnos_opcion_seleccionada == 6:
                break

    def _submenuGestionTurnos_listados_por_filtro(self):
        submenu_turnos_por_filtro = Menu(["Listado completo (ordenado por id)", "Listado por paciente", "Listado por medico", "Volver"])

        while True:
            submenu_turnos_por_filtro.mostrarMenu("tipos de listados")

            submenu_turnos_por_filtro_opcion_seleccionada = submenu_turnos_por_filtro.pedirOpcionDeMenuValida()
            if submenu_turnos_por_filtro_opcion_seleccionada == 1:
                self.gestor_turnos.listarTurnos()
            elif submenu_turnos_por_filtro_opcion_seleccionada == 2:
                self.gestor_turnos.listar_turnos_filtrados("paciente")
            elif submenu_turnos_por_filtro_opcion_seleccionada == 3:
                self.gestor_turnos.listar_turnos_filtrados("medico")
            elif submenu_turnos_por_filtro_opcion_seleccionada == 4:
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
                self._submenuGestionTurnos()
            elif menu_principal_opcion_seleccionada == 4:
                print("\n Hasta luego!")
                break
            
            input("\nPresione Enter para continuar. ")

main = Main()
main.ejecutar()