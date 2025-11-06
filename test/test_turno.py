import unittest
from datetime import datetime
from app.models.turno import Turno
from app import db, create_app

class TurnoTestCase(unittest.TestCase):
    # Tests que verifican creación y actualización de Turno

    def setUp(self):
        # Preparar app en modo testing y crear tablas
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        # Limpiar DB y contexto
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_creacion_turno(self):
        # Insertar turno y comprobar que existe en la DB
        turno = Turno(
            fecha=datetime(2025, 8, 21, 10, 30), 
            estado="disponible"
        )
        db.session.add(turno)
        db.session.commit()

        turno_db = Turno.query.first()
        self.assertIsNotNone(turno_db)
        self.assertEqual(turno_db.estado, "disponible")

    def test_actualizar_estado(self):
        # Cambiar estado y verificar persistencia
        turno = Turno(
            fecha=datetime(2025, 8, 21, 10, 30),
            estado="disponible"
        )
        db.session.add(turno)
        db.session.commit()

        turno.estado = "ocupado"
        db.session.commit()

        turno_db = Turno.query.first()
        self.assertEqual(turno_db.estado, "ocupado")

if __name__ == '__main__':
    unittest.main()
