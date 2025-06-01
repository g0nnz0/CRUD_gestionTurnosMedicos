import pickle
import os
from clasesModelo import Paciente


class GestorPacientes:
    def __init__(self, nombreArchivoPacientes: str):
        self.nombreArchivoPacientes = nombreArchivoPacientes
        self.listaDePacientes = self._cargarListaPacientes()
        

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


    def agregarPaciente(self):
        pass

    def listarPacientes(self):
        pass

    def modificarPaciente(self):
        pass
