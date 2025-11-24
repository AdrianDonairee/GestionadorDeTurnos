import unittest
from flask import current_app
from app import create_app, db
from sqlalchemy import text
import os

class DbTestCase(unittest.TestCase):
    """Pruebas para verificar la configuración y conexión a la base de datos."""

    def setUp(self):
        """Crear la aplicación en modo `testing` y preparar el contexto."""
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        """Crear todas las tablas necesarias para las pruebas."""
        db.create_all()

    def tearDown(self):
        """Limpiar la base de datos y el contexto tras la prueba."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        """Verifica que la aplicación Flask existe en el contexto."""
        self.assertIsNotNone(current_app)

    def test_db_connection(self):
        """Ejecuta una consulta simple para confirmar que la BD responde."""
        result = db.session.query(text("'hello world'")) .one()
        self.assertEqual(result[0], 'hello world')


if __name__ == '__main__':
    unittest.main()
