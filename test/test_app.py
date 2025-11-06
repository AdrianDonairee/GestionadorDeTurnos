import unittest
from flask import current_app
from app import create_app
import os

# Test básico: verificar que la aplicación Flask se crea correctamente

class AppTestCase(unittest.TestCase):

    def setUp(self):
        # Preparar contexto de Flask para testing
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        # Limpiar contexto de Flask
        self.app_context.pop()

    def test_app(self):
        # La aplicación debe existir en el contexto
        self.assertIsNotNone(current_app)

if __name__ == '__main__':
    unittest.main()