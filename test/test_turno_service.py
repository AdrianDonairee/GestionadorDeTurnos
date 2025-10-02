import unittest
from datetime import date, time
from app import create_app, db
from app.models.turno import Turno
from app.services.turno_service import TurnoService

class TestTurnoService(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.turno = Turno(
            fecha=date(2025, 9, 25),
            hora=time(10, 0)
        )

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_turno(self):
        created = TurnoService.create(self.turno)
        self.assertEqual(created.fecha, self.turno.fecha)
        self.assertEqual(created.hora, self.turno.hora)
        self.assertEqual(created.estado, "disponible")

    def test_get_by_id(self):
        TurnoService.create(self.turno)
        found = TurnoService.get_by_id(1)
        self.assertIsNotNone(found)

    def test_read_all(self):
        TurnoService.create(self.turno)
        turnos = TurnoService.read_all()
        self.assertTrue(any(t.fecha == self.turno.fecha and t.hora == self.turno.hora for t in turnos))

    def test_update_turno(self):
        TurnoService.create(self.turno)
        self.turno.estado = "reservado"
        updated = TurnoService.update(self.turno)
        self.assertEqual(updated.estado, "reservado")

    def test_delete_turno(self):
        TurnoService.create(self.turno)
        TurnoService.delete(1)
        found = TurnoService.get_by_id(1)
        self.assertIsNone(found)

if __name__ == "__main__":
    unittest.main()
