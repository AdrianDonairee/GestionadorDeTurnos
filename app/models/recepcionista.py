from dataclasses import dataclass
from app import db

@dataclass
class Recepcionista(db.Model):
    """Modelo `Recepcionista`.

    Representa a una recepcionista del consultorio.
    Atributos principales: `id`, `nombre`, `email`.
    """
    __tablename__ = "recepcionistas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre: str = db.Column(db.String(30), nullable=False)
    email: str = db.Column(db.String(150), nullable=False)
