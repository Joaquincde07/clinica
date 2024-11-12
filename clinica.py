from datetime import date

class clinica:
    def Agregar(self):
        print(f"{self.__class__.__name__} agregado correctamente")
    
    def Modificar(self):
        print(f"{self.__class__.__name__} modificado correctamente")
    
    def Eliminar(self):
        print(f"{self.__class__.__name__} eliminado correctamente")
        
    def ListaDeConsulta(self):
        print(f"Listado: \n{self.__class__.__name__}")

class Paciente(clinica):
    def __init__(self, id: str, nombre: str, edad: int, genero: str, email: str, telefono: str, direccion: str):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
    
    def ListaDeConsulta(self):
        print(f"Paciente: {self.nombre} - ID: {self.id}")

class Quimico(clinica):
    def __init__(self, id: str, nombre: str, direccion: str, email: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
    
    def EntregaMedicamentos(self):
        print(f"Medicamentos entregados por {self.nombre}")
 
class Laboratorio(clinica):
    def __init__(self, id: str, nombre: str, direccion: str, email: str, telefono: str):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.telefono = telefono
    
    def RecolectarPrueba(self):
        print(f"Prueba recolectada por {self.nombre}")
    
    def GenerarInformeLaboral(self):
        print(f"Informe de laboratorio generado por {self.nombre}")

class Descripcion:
    def __init__(self, idPrescripcion: int, diagnostico: str, nombreMedicina: str, potenciaMedicamento: int, 
                 frecuenciaMedicamento: int, observaciones: str, pruebaLaboratorio: str, laboratorioInstrucciones: str, 
                 preincripcionesEntregar: str, solicitudesLaboratorioRealizadas: str, montoFactura: float):
        self.idPrescripcion = idPrescripcion
        self.diagnostico = diagnostico
        self.nombreMedicina = nombreMedicina
        self.potenciaMedicamento = potenciaMedicamento
        self.frecuenciaMedicamento = frecuenciaMedicamento
        self.observaciones = observaciones
        self.pruebaLaboratorio = pruebaLaboratorio
        self.laboratorioInstrucciones = laboratorioInstrucciones
        self.preincripcionesEntregar = preincripcionesEntregar
        self.solicitudesLaboratorioRealizadas = solicitudesLaboratorioRealizadas
        self.montoFactura = montoFactura

    def GenerarFactura(self):
        print(f"Factura generada con monto: {self.montoFactura}")
        
class Doctores(clinica, Descripcion):
    def __init__(self, id: str, nombre: str, edad: int, genero: str, calificacion: str, experiencia: str, numeroRegistro: str):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.calificacion = calificacion
        self.experiencia = experiencia
        self.numeroRegistro = numeroRegistro
    
        self.descripcion = None

    def AsignarDescripcion(self, descripcion: Descripcion):
        self.descripcion = descripcion
    
    def MostrarInformacion(self):
        print(f"Doctor: {self.nombre}, Calificación: {self.calificacion}, Registro: {self.numeroRegistro}")

class Consultas:
    def __init__(self, paciente: Paciente, doctor: Doctores, en_linea_o_cita: str, fecha_solicitud: date, 
                 cadena_sintomas: str, estado_solicitud: str):
        self.paciente = paciente
        self.doctor = doctor
        self.en_linea_o_cita = en_linea_o_cita
        self.fecha_solicitud = fecha_solicitud
        self.cadena_sintomas = cadena_sintomas
        self.estado_solicitud = estado_solicitud

    def MostrarConsulta(self):
        print(f"Consulta para {self.paciente.nombre} con el Dr. {self.doctor.nombre} el {self.fecha_solicitud}")
        print(f"Sintomas: {self.cadena_sintomas} - Estado: {self.estado_solicitud}")

class Especialista(Doctores):
    def __init__(self, id: str, nombre: str, edad: int, genero: str, calificacion: str, experiencia: str, numeroRegistro: str, 
                 especialidad: str):
        super().__init__(id, nombre, edad, genero, calificacion, experiencia, numeroRegistro)
        self.especialidad = especialidad

    def MostrarEspecialidad(self):
        print(f"Especialista en {self.especialidad}")
