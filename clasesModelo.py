from datetime import datetime
import re

class Fecha:
    def __init__(self, fecha_str: str = None):
        if not fecha_str:
            hoy = datetime.now()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            if not self.es_fecha_valida(fecha_str):
                raise ValueError(
                    'Formato de fecha no válido. Debe ser dd/mm/aaaa')
            partes = str(fecha_str).split('/')
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])

    def es_fecha_valida(self, fecha: str):
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        return re.match(patron, fecha)

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

class FechaHora:
    def __init__(self, fecha_hora_str: str = None):
        if not fecha_hora_str:
            ahora = datetime.now()
            self.dia = ahora.day
            self.mes = ahora.month
            self.anio = ahora.year
            self.hora = ahora.hour
            self.minuto = ahora.minute
        else:
            if not self.es_fecha_hora_valida(fecha_hora_str):
                raise ValueError('Formato no válido. Debe ser "dd/mm/aaaa HH:MM"')
            fecha_str, hora_str = fecha_hora_str.strip().split()
            self.dia, self.mes, self.anio = map(int, fecha_str.split('/'))
            self.hora, self.minuto = map(int, hora_str.split(':'))

    def es_fecha_hora_valida(self, fecha_hora: str) -> bool:
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4} ([01]\d|2[0-3]):([0-5]\d)$'
        return re.match(patron, fecha_hora) is not None

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio} {self.hora:02d}:{self.minuto:02d}"
    


class Paciente:
    def __init__(self, dni: str, nombre: str, fechaNacimiento: Fecha, obraSocial: str = None):
        self.dni = dni
        self.nombre = nombre
        self.fechaNacimiento = fechaNacimiento
        self.obraSocial = obraSocial.strip().title() if obraSocial else "Particular"
      

    def __str__(self):
        return f"Paciente {self.nombre} - Dni: {self.dni} - Fecha de Nacimiento: {self.fechaNacimiento} - Obra Social: {self.obraSocial}"




class Medico:
    def __init__(self, matricula: str, nombre: str, especialidad: str = None):
        self.matricula = matricula
        self.nombre = nombre
        self.especialidad = especialidad.strip().title() if especialidad else "Clinico"

    def __str__(self):
        return f"Medico: {self.nombre} - Matricula n°: {self.matricula} - Especialidad: {self.especialidad}"






class Turno:
    def __init__(self, fechaYHora: FechaHora, pacienteDni: str, medicoMatricula: str, MotivoTurno: str, id: int):
        self.fechaYHora = fechaYHora
        self.pacienteDni = pacienteDni
        self.medicoMatricula = medicoMatricula
        self.motivoTurno = MotivoTurno
        self.id = id

    def __str__(self):
        return f"Id: {self.id} - Horario turno: {self.fechaYHora} - Paciente dni: {self.pacienteDni} - Medico matricula n°: {self.medicoMatricula} - Motivo del Turno: {self.motivoTurno}"