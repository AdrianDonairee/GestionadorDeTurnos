from dataclasses import dataclass
@dataclass(init=True, repr=True, eq=True)
class Paciente():
    nombre:str
    apellido:str
    dni:str 
    email:str 
    fechadenacimiento:str
    telefono:str 
    