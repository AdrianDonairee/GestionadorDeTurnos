import unittest
from datetime import datetime
from app.models.turno import Turno
from app import db, create_app

class TurnoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_creacion_turno(self):
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
