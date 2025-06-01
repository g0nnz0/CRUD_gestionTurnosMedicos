import pickle
import os
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



    def agregarPaciente(self):
            try:
                dni_ingresado = self._dni_valido()
                if not self._es_dni_unico(dni_ingresado):
                    print("El dni ya existe")
                    return
            except Exception as e:
                print(f"Ocurrio un error al cargar el dni: {e}")

    def listarPacientes(self):
        pass

    def modificarPaciente(self):
        pass

