import unittest
from datetime import datetime
from app import db, create_app
from app.models.turno import Turno
from app.services.turno_service import TurnoService


class TestTurnoService(unittest.TestCase):
    """Pruebas unitarias para las operaciones del servicio de Turno.

    Cada método de `setUp`/`tearDown` y los tests individuales contienen
    docstrings que explican su propósito.
    """

    def setUp(self):
        """Preparar la aplicación en modo testing y crear las tablas."""
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Limpiar la base de datos y el contexto al finalizar cada test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_turno(self):
        """Crear un turno y verificar que se asigne un identificador."""
        turno = Turno(
            fecha=datetime(2025, 8, 21, 10, 30),
            estado="disponible"
        )
        result = TurnoService.create(turno)
        self.assertIsNotNone(result.id)

    def test_get_by_id(self):
        """Insertar un turno en la BD y recuperarlo por id."""
        turno = Turno(
            fecha=datetime(2025, 8, 21, 10, 30),
            estado="disponible"
        )
        db.session.add(turno)
        db.session.commit()

        fetched = TurnoService.get_by_id(turno.id)
        self.assertEqual(fetched.id, turno.id)

    def test_update_turno(self):
        """Actualizar el estado de un turno y verificar el cambio."""
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

