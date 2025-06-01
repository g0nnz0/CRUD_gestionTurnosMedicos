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

    
    def buscarClientePorDni(self):
        pass



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
            obra_social_ingresada = input("Ingrese la obra social del paciente (si no ingresa nada se anotará como 'Particular': ").strip()


            paciente = Paciente(dni_ingresado, nombre_ingresado, fecha_nac_valida, obra_social_ingresada)
            self.listaDePacientes.append(paciente)
            self._guardarListaPacientes()
            

    

    def modificarPaciente(self):
        pass

    
    def eliminarCliente(self):
        pass
