import unittest
from flask import current_app
from app import create_app
import os

class AppTestCase(unittest.TestCase):

    def setUp(self):
        """Preparar contexto de Flask para pruebas (modo `testing`)."""
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        """Limpiar el contexto de Flask tras cada prueba."""
        self.app_context.pop()

    def test_app(self):
        """Comprobar que la aplicación está registrada en el contexto actual."""
        self.assertIsNotNone(current_app)

if __name__ == '__main__':
    unittest.main()