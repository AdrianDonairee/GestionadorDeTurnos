from app.models import Paciente
import unittest
from flask import current_app
from app import create_app
import os

class PacienteTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_paciente(self):
        paciente = Paciente(
            nombre="Juan",
            apellido="Pérez",
            dni="12345678",
            email="juan@mail.com",
            fechadenacimiento="1990-01-01",
            telefono="2615551234"
        )

        self.assertEqual(paciente.nombre, "Juan")
        self.assertEqual(paciente.apellido, "Pérez")
        self.assertEqual(paciente.dni, "12345678")
        self.assertEqual(paciente.email, "juan@mail.com")
        self.assertEqual(paciente.fechadenacimiento, "1990-01-01")
        self.assertEqual(paciente.telefono, "2615551234")
        
if __name__ == '__main__':
    unittest.main()