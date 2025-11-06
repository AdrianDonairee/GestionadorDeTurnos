import unittest
from datetime import datetime
from app import db, create_app
from app.models.turno import Turno
from app.services.turno_service import TurnoService

class TestTurnoService(unittest.TestCase):
    # Tests para operaciones del servicio de Turno

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

    def test_create_turno(self):
        # Crear turno y validar id
        turno = Turno(
            fecha=datetime(2025, 8, 21, 10, 30),
            estado="disponible"
        )
        result = TurnoService.create(turno)
        self.assertIsNotNone(result.id)

    def test_get_by_id(self):
        # Insertar turno y obtenerlo por id
        turno = Turno(
            fecha=datetime(2025, 8, 21, 10, 30),
            estado="disponible"
        )
        db.session.add(turno)
        db.session.commit()

        fetched = TurnoService.get_by_id(turno.id)
        self.assertEqual(fetched.id, turno.id)

    def test_update_turno(self):
        # Actualizar estado de un turno
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

if __name__ == '__main__':
    unittest.main()

