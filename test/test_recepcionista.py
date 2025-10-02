from app.models.recepcionista import Recepcionista
import unittest
from flask import current_app
from app import create_app
import os

class RecepcionistaTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_recepcionista(self):
        # Instanciamos correctamente pasando los parámetros requeridos
        recepcionista = Recepcionista(nombre="Juan", email="test@um.um.edu.ar")
        self.assertIsNotNone(recepcionista)
        self.assertEqual(recepcionista.nombre, "Juan")
        self.assertEqual(recepcionista.email, "test@um.um.edu.ar")
        
if __name__ == '__main__':
    unittest.main()
