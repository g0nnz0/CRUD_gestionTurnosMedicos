import pickle
import os
from clasesModelo import Fecha
from clasesModelo import Paciente


class GestorPacientes:
    def __init__(self, nombreArchivoPacientes: str):
        self.nombreArchivoPacientes = nombreArchivoPacientes
        self.listaDePacientes: list[Paciente] = self._cargarListaPacientes()
        

    def _cargarListaPacientes(self):
        try:
            if not os.path.exists(self.nombreArchivoPacientes):
                print(f"No se encontró el archivo {self.nombreArchivoPacientes}. Se inicializa vacio")
                return []
            with open(self.nombreArchivoPacientes, "rb") as f:
                return pickle.load(f)
        except EOFError:
            print(f"El archivo {self.nombreArchivoPacientes} se inicializa vacio.")
            return []
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")


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
            while True:
                try:
                    fecha_nac_ingresada = input("Ingrese la fecha de nacimiento del paciente con el siguiente formato DD/MM/AAAA: ")
                    if not Fecha.es_fecha_valida(fecha_nac_ingresada):
                        print(f"{fecha_nac_ingresada} no es una fecha valida, intentelo nuevamente")
                        continue
                    fecha_nac_valida = Fecha(fecha_nac_ingresada)
                    break
                except ValueError as e:
                    print(f"Ocurrio un error: {e} - vuelva a intentarlo.")
                except Exception as e:
                    print(f"Ocurrio un error: {e} - vuelva a intentarlo.")



            #valido obra social
            obra_social_ingresada = input("Ingrese la obra social del paciente (si no ingresa nada se anotará como 'Particular': ").strip().title()


            paciente = Paciente(dni_ingresado, nombre_ingresado, fecha_nac_valida, obra_social_ingresada)
            self.listaDePacientes.append(paciente)
            self._guardarListaPacientes()
            

    
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

        dni_ingresado = self._dni_valido()
        for paciente in self.listaDePacientes:
            if dni_ingresado == paciente.dni:
                print(f"Paciente encontrado: {paciente}")
                opcion_seleccionada = input("Para confirmar la eliminación presione 'S', para cancelar presione 'N': ").strip().upper()
                if opcion_seleccionada == 'S':
                    self.listaDePacientes.remove(paciente)
                    self._guardarListaPacientes()
                    print(f"El paciente: {paciente}. Fué eliminado exitosamente de la base de datos.")
                    break
                elif opcion_seleccionada == 'N':
                    print("No se efectuaron cambios.")
                    return
                else:
                    print("Opción no valida. No se efectuaron cambios")

