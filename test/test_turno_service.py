import unittest
from datetime import datetime
from app import db, create_app
from app.models.turno import Turno
from app.services.turno_service import TurnoService

class TestTurnoService(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_turno(self):
        turno = Turno(
            fecha=datetime(2025, 8, 21, 10, 30),
            estado="disponible"
        )
        result = TurnoService.create(turno)
        self.assertIsNotNone(result.id)

    def test_get_by_id(self):
        turno = Turno(
            fecha=datetime(2025, 8, 21, 10, 30),
            estado="disponible"
        )
        db.session.add(turno)
        db.session.commit()

        fetched = TurnoService.get_by_id(turno.id)
        self.assertEqual(fetched.id, turno.id)

    def test_update_turno(self):
        turno = Turno(
            fecha=datetime(2025, 8, 21, 10, 30),
            estado="disponible"
        )
        db.session.add(turno)
        db.session.commit()

        turno.estado = "ocupado"
        db.session.commit()

        fetched = Turno.query.get(turno.id)
        self.assertEqual(fetched.estado, "ocupado")

