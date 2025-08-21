from dataclasses import dataclass
@dataclass(init=False)
class Paciente():
    nombre:str 
    email:str 
    edad:str
    telefono:str 