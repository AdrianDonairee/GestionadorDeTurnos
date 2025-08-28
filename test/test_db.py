import unittest
from flask import current_app
from app import create_app, db
from sqlalchemy import text
import os

class DbTestCase(unittest.TestCase):

    def setUp(self):
        # Indicar que se quiere usar la configuración de testing
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        
        # Crear todas las tablas antes de cada test
        db.create_all()

    def tearDown(self):
        # Limpiar la base de datos después de cada test
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        # Verifica que la app existe
        self.assertIsNotNone(current_app)

    def test_db_connection(self):
        # Verifica que la base de datos funciona ejecutando un query simple
        result = db.session.query(text("'hello world'")).one()
        self.assertEqual(result[0], 'hello world')


if __name__ == '__main__':
    unittest.main()
