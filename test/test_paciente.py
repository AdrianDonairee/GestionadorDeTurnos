from datetime import date
from app.models import Paciente
import unittest
from flask import current_app
from app import create_app
from app.services import PacienteService
from app import db
import os

class PacienteTestCase(unittest.TestCase):
    """Pruebas para la entidad `Paciente`: crear, leer, actualizar y borrar."""

    def setUp(self):
        """Configurar la aplicación en modo `testing` y crear las tablas
        necesarias antes de cada prueba."""
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        """Crear todas las tablas antes de cada prueba."""
        db.create_all()

    def tearDown(self):
        """Limpiar la base de datos y el contexto al finalizar cada prueba."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        """Verificar que la aplicación Flask está disponible en el contexto."""
        self.assertIsNotNone(current_app)
        
    def test_registrar_paciente(self):
        """Registrar un paciente y validar los campos persistidos."""
        paciente = self._registrar_paciente()

        self.assertEqual(paciente.id, 1)
        self.assertEqual(paciente.nombre, "Juan")
        self.assertEqual(paciente.apellido, "Pérez")
        self.assertEqual(paciente.fechadenacimiento, date(1990, 12, 31))
        self.assertEqual(paciente.dni, "12345678")

    def test_obtener_paciente(self):
        """Recuperar un paciente por id y comprobar sus datos."""
        paciente = self._registrar_paciente()
        paciente = PacienteService.get_by_id(paciente.id)
        self.assertIsNotNone(paciente)
        self.assertEqual(paciente.apellido, "Pérez")

    def test_obtener_pacientes(self):
        """Comprobar que la lista de pacientes devuelve los registros creados."""
        self._registrar_paciente()
        pacientes = PacienteService.read_all()
        self.assertEqual(len(pacientes), 1)

    def test_actualizar_paciente(self):
        """Actualizar campos de un paciente y verificar que se guarden."""
        paciente = self._registrar_paciente()
        paciente.nombre = "Carlos"
        paciente.apellido = "Gomez"
        paciente.dni = "87654321"
        paciente.email = "carlos@mail.com"
        paciente.fechadenacimiento = date(1995, 12, 30)
        paciente.telefono = "2615554321"

        paciente = PacienteService.update(paciente)
        self.assertEqual(paciente.nombre, "Carlos")
        self.assertEqual(paciente.apellido, "Gomez")
        self.assertEqual(paciente.dni, "87654321")
        self.assertEqual(paciente.email, "carlos@mail.com")
        self.assertEqual(paciente.fechadenacimiento, date(1995, 12, 30))
        self.assertEqual(paciente.telefono, "2615554321")
        return paciente

    def _registrar_paciente(self):
        paciente = Paciente()
        paciente.nombre = "Juan"
        paciente.apellido = "Pérez"
        paciente.dni = "12345678"
        paciente.email = "juan@mail.com"
        paciente.fechadenacimiento = date(1990, 12, 31)
        paciente.telefono = "2615551234"

        paciente = PacienteService.create(paciente)
        return paciente

    def test_eliminar_paciente(self):
        """Eliminar un paciente y confirmar que ya no puede recuperarse."""
        paciente = self._registrar_paciente()
        eliminado = PacienteService.delete(paciente.id)
        self.assertTrue(eliminado)
        paciente = PacienteService.get_by_id(paciente.id)
        self.assertIsNone(paciente)

if __name__ == '__main__':
    unittest.main()