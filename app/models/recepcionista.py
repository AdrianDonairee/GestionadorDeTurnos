from dataclasses import dataclass

@dataclass
class Recepcionista(db.Model):
    __tablename__="recepcionistas"
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    nombre:str = db.Column(db.String(30), nullable=False)
    email:str = db.Column(db.String(150), nullable=False)
