from marshmallow import Schema, fields, post_load
from app.models import Paciente

class PacienteSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    dni = fields.Str(required=True)
    telefono = fields.Str()
    email = fields.Email()
    fecha_de_nacimiento = fields.Date()
    
    @post_load
    def make_paciente(self, data, **kwargs):
        return Paciente(**data)