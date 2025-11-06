from datetime import date
from app.models import Paciente
import unittest
from flask import current_app
from app import create_app
from app.services import PacienteService
from app import db
import os

class PacienteTestCase(unittest.TestCase):
    # Tests para la entidad Paciente: crear, leer, actualizar y borrar

    def setUp(self):
        # Preparar app en modo testing y crear tablas
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
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
        # Verificar que la app existe
        self.assertIsNotNone(current_app)
        
    def test_registrar_paciente(self):
        # Registrar paciente y validar campos
        paciente = self._registrar_paciente()

        self.assertEqual(paciente.id, 1)
        self.assertEqual(paciente.nombre, "Juan")
        self.assertEqual(paciente.apellido, "Pérez")
        self.assertEqual(paciente.fechadenacimiento, date(1990, 12, 31))
        self.assertEqual(paciente.dni, "12345678")

    def test_obtener_paciente(self):
        # Obtener paciente por id
        paciente = self._registrar_paciente()
        paciente = PacienteService.get_by_id(paciente.id)
        self.assertIsNotNone(paciente)
        self.assertEqual(paciente.apellido, "Pérez")

    def test_obtener_pacientes(self):
        # Listar pacientes
        self._registrar_paciente()
        pacientes = PacienteService.read_all()
        self.assertEqual(len(pacientes), 1)

    def test_actualizar_paciente(self):
        # Actualizar campos de un paciente
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
        # Eliminar paciente y comprobar que ya no existe
        paciente = self._registrar_paciente()
        eliminado = PacienteService.delete(paciente.id)
        self.assertTrue(eliminado)
        paciente = PacienteService.get_by_id(paciente.id)
        self.assertIsNone(paciente)

if __name__ == '__main__':
    unittest.main()