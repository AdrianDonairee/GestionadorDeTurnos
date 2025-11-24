import unittest
from datetime import datetime
from app.models.turno import Turno
from app import db, create_app

class TurnoTestCase(unittest.TestCase):
    """Pruebas unitarias que verifican la creación y actualización de Turno."""

    def setUp(self):
        """Configurar la aplicación en modo `testing` y crear las tablas
        antes de cada prueba."""
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """Eliminar el contexto y limpiar la base de datos tras la prueba."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_creacion_turno(self):
        """Insertar un turno y comprobar que queda persistido en la BD."""
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
        """Cambiar el estado de un turno existente y verificar persistencia."""
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
