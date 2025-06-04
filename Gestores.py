import pickle
import os
from clasesModelo import Fecha
from clasesModelo import FechaHora
from clasesModelo import Paciente
from clasesModelo import Medico
from clasesModelo import Turno


class GestorPacientes:
    def __init__(self, nombreArchivoPacientes: str):
        self.nombreArchivoPacientes = nombreArchivoPacientes
        self.listaDePacientes: list[Paciente] = self._cargarListaPacientes()
        

    def _cargarListaPacientes(self):
        
        if not os.path.exists(self.nombreArchivoPacientes):
            print(f"No se encontró el archivo {self.nombreArchivoPacientes}. Se inicializa vacio")
            return []
        try:
            with open(self.nombreArchivoPacientes, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            print(f"El archivo {self.nombreArchivoPacientes} se inicializa vacio.")
            return []
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")
            return []


    def _guardarListaPacientes(self):
        try:
            with open(self.nombreArchivoPacientes, "wb") as f:
                pickle.dump(self.listaDePacientes, f)
                print("El archivo se guardó correctamente.")
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")


    #metodos auxiliares para validacion de dni
    def _dni_valido(self, mensaje = "Ingrese el dni del paciente: ") -> str:
        while True:
            dni_validado = input(mensaje).strip()
            if not dni_validado.isdigit() or len(dni_validado) < 7:
                print("El dni tiene que ser numerico y tener al menos 7 digitos")
                continue
            return dni_validado
    
    def _es_dni_unico(self, dni) -> bool:
        for paciente in self.listaDePacientes:
            if dni == paciente.dni:
                return False
        return True
    
    #metodos aux para validar fecha reforzando los metodos de la class Fecha y manteniendo division de responsabilidades
    def _es_fecha_nacimiento_valida(self, fecha_str: str) -> bool:
        try:
            #Acá le delego a al constructor que verifique si fecha_str está bien formateada
            Fecha(fecha_str)
            #si lo está me devuelve True, el cual voy a usar como condicion en la funcion de abajo
            return True
        except ValueError:
            #Si el constructor de Fecha detecta un error, saltará acá, devolviendome False
            return False
    
    def _pedir_fecha_nacimiento_valida(self) -> Fecha:
        #acá hay una estructura similar a la que usé en la clase Menu, una especie de do while
        fecha_nacimiento_ingresada = "NO_VALIDA"
        while not self._es_fecha_nacimiento_valida(fecha_nacimiento_ingresada):
            fecha_nacimiento_ingresada = input("Ingrese la fecha de nacimiento del paciente (dd/mm/aaaa): ")
            if not self._es_fecha_nacimiento_valida(fecha_nacimiento_ingresada):
                print("Formato de fecha invalido. Debe ser dd/mm/aaaa")
        return Fecha(fecha_nacimiento_ingresada)


    #CRUD: Read
    def listarPacientes(self):
        if not self.listaDePacientes:
            print("No hay pacientes cargados en este momento.")
            return
        for paciente in self.listaDePacientes:
            print(paciente)

    #CRUD: Read
    def buscarPacientePorDni(self) -> Paciente:
        dni_ingresado = self._dni_valido()
        for paciente in self.listaDePacientes:
            if dni_ingresado == paciente.dni:
                print(f"Coincidencia exitosa.")
                print(paciente)
                return paciente
        print(f"No se encontró paciente con dni: {dni_ingresado}.")
        return None



    #CRUD: Create
    def agregarPaciente(self):
            
            #valido dni
            dni_ingresado = self._dni_valido()
            if not self._es_dni_unico(dni_ingresado):
                print("Ya existe un paciente con ese dni.")
                return
           
            #valido nombre
            while True:
                try:
                    nombre_ingresado = input("Ingrese el nombre del paciente: ").strip().title()
                    if nombre_ingresado == "":
                        print("Este campo no puede estar vacio")
                        continue
                    break
                except Exception as e:
                    print(f"Ocurrio un error inesperado al cargar el nombre: {e}")

            #valido fecha de nacimiento
            #Arreglé el bug, estaba llamando metodos de la clase Fecha directamente desde acá
            #si bien validaban el str fecha, no los devolvian, y me hacia ruido tener que poner self como argumento
            #y claro, era porque no era ni una instancia, estaba accediendo directamente a la clase fecha
            #cuando como mucho tengo que usar su constructor(como el los metodos auxiliares para pedir fecha de este gestor)
            fecha_nac_valida = self._pedir_fecha_nacimiento_valida()



            #valido obra social
            obra_social_ingresada = input("Ingrese la obra social del paciente (si no ingresa nada se anotará como 'Particular': ").strip().title()


            paciente = Paciente(dni_ingresado, nombre_ingresado, fecha_nac_valida, obra_social_ingresada)
            self.listaDePacientes.append(paciente)
            self._guardarListaPacientes()
            print("Nuevo paciente agregado exitosamente.")
            

    
    #CRUD: Update
    def modificarPaciente(self):
        paciente_a_modificar = self.buscarPacientePorDni()
        if not paciente_a_modificar:
            return
        
        #modficar nombre
        while True:
            try:
                paciente_nuevo_nombre = input(f"Ingrese el nuevo nombre del paciente. -Nombre actual: {paciente_a_modificar.nombre} - (si no quiere modificarlo presione Enter): ").strip()
                if paciente_nuevo_nombre == "":
                    print("No se modificó el nombre")
                    break
                if paciente_nuevo_nombre.isdigit():
                    print("El nombre no puede tener numeros")
                    continue
                paciente_a_modificar.nombre = paciente_nuevo_nombre.title()
                print(f"Modificacion de nombre exitosa. -Nuevo nombre: {paciente_a_modificar.nombre} -")
            except Exception as e:
                print(f"Ocurrio un error inesperado: {e}")

        #modificar fecha de nacimiento
        while True:
            try:
                nueva_fecha_nacimiento_ingresada = input(f"Ingrese la nueva fecha de nacimiento del paciente con formato DD/MM/AAAA -Fecha de nacimiento actual: {paciente_a_modificar.fechaNacimiento} - (si no quiere modificar presione Enter): ")
                if nueva_fecha_nacimiento_ingresada == "":
                    print("No se modificó la fecha de nacimiento.")
                    break
                if not Fecha.es_fecha_valida(nueva_fecha_nacimiento_ingresada):
                    print(f"{nueva_fecha_nacimiento_ingresada} no es una fecha valida, intentelo nuevamente")
                    continue
                nueva_fecha_nac_valida = Fecha(nueva_fecha_nacimiento_ingresada)
                paciente_a_modificar.fechaNacimiento = nueva_fecha_nac_valida
                print(f"Modificación de fecha de nacimineto exitosa. -Nueva fecha de nacimiento: {paciente_a_modificar.fechaNacimiento}-")
                break
            except ValueError as e:
                    print(f"Ocurrió un error: {e} - vuelva a intentarlo.")
            except Exception as e:
                    print(f"Ocurrió un error: {e} - vuelva a intentarlo.")
        
        #modificar obra social
        nueva_obra_social_ingresada = input(f"Ingrese la nueva obra social -Obra social actual: {paciente_a_modificar.obraSocial}-(si no quiere modificar presione Enter): ").strip()
        if nueva_obra_social_ingresada == "":
            print("No se modificó la obra social")
        if nueva_obra_social_ingresada:
            paciente_a_modificar.obraSocial = nueva_obra_social_ingresada.title()
            print(f"Modificación de obra social exitosa. -Nueva obra social: {paciente_a_modificar.obraSocial} -")

        self._guardarListaPacientes()
        print(f"Modificacion de paciente: {paciente_a_modificar.nombre} - Dni: {paciente_a_modificar.dni} - Fecha de nacimiento: {paciente_a_modificar.fechaNacimiento} - Obra social: {paciente_a_modificar.obraSocial} Exitosa!")

            

    #CRUD: Delete
    def eliminarPaciente(self):
        if not self.listaDePacientes:
            print("No hay pacientes cargados")
            return

        paciente_ingresado = self.buscarPacientePorDni()
        if paciente_ingresado:
            opcion_seleccionada = input("Para confirmar la eliminación presione 'S', para cancelar presione 'N': ").strip().upper()
            if opcion_seleccionada == 'S':
                self.listaDePacientes.remove(paciente_ingresado)
                self._guardarListaPacientes()
                print(f"El {paciente_ingresado}. Fué eliminado exitosamente de la base de datos.")
            elif opcion_seleccionada == 'N':
                print("No se efectuaron cambios.")
                return
            else:
                print("Opción no valida. No se efectuaron cambios")



class GestorMedicos:
    def __init__(self, nombreArchivoMedicos: str):
        self.nombreArchivoMedicos = nombreArchivoMedicos
        self.listaDeMedicos: list[Medico] = self._cargarListaMedicos()


    def _cargarListaMedicos(self):
        
        if not os.path.exists(self.nombreArchivoMedicos):
            print(f"No se encontró el archivo {self.nombreArchivoMedicos}. Se inicializa vacio")
            return []
        try:
            with open(self.nombreArchivoMedicos, "rb") as f:
                return pickle.load(f)
        except EOFError:
            print(f"El archivo {self.nombreArchivoMedicos} se inicializa vacio.")
            return []
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")
            return []
    
    def _guardarListaMedicos(self):
        try:
            with open(self.nombreArchivoMedicos, "wb") as f:
                pickle.dump(self.listaDeMedicos, f)
                print("El archivo se guardó correctamente.")
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")


     #metodos auxiliares para validacion de matricula
    def _matricula_valida(self, mensaje = "Ingrese la matricula del medico: ") -> str:
        while True:
            matricula_validada = input(mensaje).strip()
            if len(matricula_validada) < 6:
                print("La matricula debe tener al menos tener al menos 6 digitos")
                continue
            return matricula_validada
    
    def _es_matricula_unica(self, matricula) -> bool:
        for medico in self.listaDeMedicos:
            if matricula == medico.matricula:
                return False
        return True



    def listarMedicos(self):
        if not self.listaDeMedicos:
            print("No hay medicos cargados en este momento.")
            return
        for medico in self.listaDeMedicos:
            print(medico)


    def buscarMedicoPorMatricula(self) -> Medico:
        matricula_ingresada = self._matricula_valida()
        for medico in self.listaDeMedicos:
            if matricula_ingresada == medico.matricula:
                print(f"Coincidencia exitosa.")
                print(medico)
                return medico
        print(f"No se encontró medico con matricula: {matricula_ingresada}.")
        return None


    def agregarMedico(self):
            
            matricula_ingresada = self._matricula_valida()
            if not self._es_matricula_unica(matricula_ingresada):
                print("Ya existe un medico con esa matricula.")
                return
           
            
            while True:
                try:
                    nombre_ingresado = input("Ingrese el nombre del medico: ").strip().title()
                    if nombre_ingresado == "":
                        print("Este campo no puede estar vacio")
                        continue
                    break
                except Exception as e:
                    print(f"Ocurrio un error inesperado al cargar el nombre: {e}")


            especialidad_ingresada = input("Ingrese la especialidad del medico (si no ingresa nada se anotará como 'Clinico': ").strip().title()

            medico = Medico(matricula_ingresada, nombre_ingresado, especialidad_ingresada)
            self.listaDeMedicos.append(medico)
            self._guardarListaMedicos()
            print("Nuevo medico agregado exitosamente.")
            print(f"Nombre: {medico.nombre} - Matricula {medico.matricula} - Especialidad: {medico.especialidad}")



    def modificarMedico(self):
        medico_a_modificar = self.buscarMedicoPorMatricula()
        if not medico_a_modificar:
            return
        
        #modficar nombre
        while True:
            try:
                medico_nuevo_nombre = input(f"Ingrese el nuevo nombre del medico. -Nombre actual: {medico_a_modificar.nombre} - (si no quiere modificarlo presione Enter): ").strip()
                if medico_nuevo_nombre == "":
                    print("No se modificó el nombre")
                    break
                if medico_nuevo_nombre.isdigit():
                    print("El nombre no puede tener numeros")
                    continue
                medico_a_modificar.nombre = medico_nuevo_nombre.title()
                print(f"Modificacion de nombre exitosa. -Nuevo nombre: {medico_a_modificar.nombre} -")
                break
            except Exception as e:
                print(f"Ocurrio un error inesperado: {e}")

        
        #modificar especialidad
        nueva_especialidad = input(f"Ingrese la nueva Especialidad - Especialidad actual: {medico_a_modificar.especialidad}-(si no quiere modificar presione Enter): ").strip()
        if nueva_especialidad == "":
            print("No se modificó especialidad")
        medico_a_modificar.especialidad = nueva_especialidad.title()
        print(f"Modificación de especialidad exitosa. -Nueva especialidad: {medico_a_modificar.especialidad} -")

        self._guardarListaMedicos()
        print(f"Modificacion de medico: {medico_a_modificar.nombre} - Matricula {medico_a_modificar.matricula} - Especialidad: {medico_a_modificar.especialidad} Exitosa!")

    def eliminarMedico(self):
        if not self.listaDeMedicos:
            print("No hay medicos cargados")
            return

        medico_ingresado = self.buscarMedicoPorMatricula()
        if medico_ingresado:
            opcion_seleccionada = input("Para confirmar la eliminación presione 'S', para cancelar presione 'N': ").strip().upper()
            if opcion_seleccionada == 'S':
                self.listaDeMedicos.remove(medico_ingresado)
                self._guardarListaMedicos()
                print(f"El {medico_ingresado}. Fué eliminado exitosamente de la base de datos.")
            elif opcion_seleccionada == 'N':
                print("No se efectuaron cambios.")
                return
            else:
                print("Opción no valida. No se efectuaron cambios")



class GestorTurnos:
    #en este caso implemento inyeccion de dependecias
    #(tambien aprendí que puedo pasar los gestores como string, para codigos mas modulares, en este caso no hace falta)
    def __init__(self, nombreArchivoTurnos: str, gestor_pacientes: GestorPacientes, gestor_medicos: GestorMedicos):
        self.nombreArchivoTurnos = nombreArchivoTurnos
        self.listaDeTurnos: list[Turno] = self._cargarListaTurnos()
        self.gestor_pacientes = gestor_pacientes
        self.gestor_medicos = gestor_medicos


    def _cargarListaTurnos(self):
        if not os.path.exists(self.nombreArchivoTurnos):
            print(f"No se encontró el archivo {self.nombreArchivoTurnos}. Se inicializa vacio")
            return []

        try:
            with open(self.nombreArchivoTurnos, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            print(f"El archivo {self.nombreArchivoTurnos} se inicializa vacio.")
            return []
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")
            return []



    def _guardarListaTurnos(self):
        try:
            with open(self.nombreArchivoTurnos, "wb") as f:
                pickle.dump(self.listaDeTurnos, f)
                print("El archivo se guardó correctamente")
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")

    #metodos auxiliares
    #ambos son modificaciones de las validaciones para fecha del gestorPacientes
    def _es_fecha_y_hora_valida(self, fecha_y_hora_str: str) -> bool:
        try:
            FechaHora(fecha_y_hora_str)
            return True
        except ValueError:
            return False
    
    def _pedir_fecha_y_hora_valida(self) -> FechaHora:
        fecha_y_hora_ingresada = "NO_VALIDA"
        while not self._es_fecha_y_hora_valida(fecha_y_hora_ingresada):
            fecha_y_hora_ingresada = input("Ingrese la fecha y la hora del turno ('dd/mm/aaaa HH:MM'): ")
            if not self._es_fecha_y_hora_valida(fecha_y_hora_ingresada):
                print("Formato de fecha y hora invalido. Debe ser dd/mm/aaaa HH:MM")
        return FechaHora(fecha_y_hora_ingresada)


    #ES BOCETO AUN, REVISAR
    def agregarTurno(self):
        #aca la peticion de fecha y hora es sencilla porque toda la validacion está en los metodos aux
        fecha_y_hora_ingresada = self._pedir_fecha_y_hora_valida()

        #busqueda de paciente usando metodos del gestor de pacientes
        dni_ingresado = self.gestor_pacientes.buscarPacientePorDni()
        if not dni_ingresado:
            print(f"No se encontró el paciente. Debe registrarlo desde el menú Gestión de Pacientes.")
            return
        
        #busqueda del medico usando metodos del gestor de medicos
        matricula_ingresada = self.gestor_medicos.buscarMedicoPorMatricula()
        if not matricula_ingresada:
            print(f"No se encontró el medico. Debe registrarlo desde el menú Gestión de Medicos.")
            return
        
        motivo_ingresado = input("Ingrese el motivo de su turno: ")

        turno = Turno(fecha_y_hora_ingresada, dni_ingresado, matricula_ingresada, motivo_ingresado)
        self.listaDeTurnos.append(turno)

        




    def evitarSolapamientoTurnos(self):
        print("evitarSolapamientoTurnos alcanzada")
        pass

    def listarTurnos(self):
        print("listarTurnos alcanzado")
        pass

    def listarTurnoPorPacienteOMedico(self):
        print("listarTurnoPorPacienteOMedico alcanzado")
        pass

    def buscarTurnoPorFecha(self):
        print("buscarTurnoPorFecha alcanzado")
        pass


    

    def eliminarTurno(self):
        print("EliminarTurno alcanzado")
        pass




