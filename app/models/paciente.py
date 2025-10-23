from .venv.Lib.site-packages.sqlalchemy.sql._typing import Nullable
from .venv.Lib.site-packages.sqlalchemy.sql.schema import PrimaryKeyConstraint
from dataclasses import dataclass

@dataclass(init=True, repr=True, eq=True)
class Paciente(db.Model):
    __tablename__ = "pacientes"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nombre:str = db.Column(db.String(30), nullable=False)
    apellido:str = db.Column(db.String(30), nullable=False)
    dni:str = db.Column(db.String(10), nullable=False)
    email:str = db.Column(db.String(150), nullable=False)
    fechadenacimiento = db.Column(db.Date, nullable=False)
    telefono:str = db.Column(db.String(20), nullable=False)
    