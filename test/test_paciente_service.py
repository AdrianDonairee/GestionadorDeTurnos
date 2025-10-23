import unittest
from app.services import PacienteService


class TestPacienteService(unittest.TestCase):
    def setUp(self):
        
        self.service = PacienteService()
    def test_registrar_paciente(self):
        paciente_id, paciente = self.service.registrar_paciente(
            "Juan", "Pérez", "12345678", "juan@mail.com", "1990-01-01", "2615551234"
        )
        self.assertEqual(paciente_id, 1)
        self.assertEqual(paciente.nombre, "Juan")
        self.assertEqual(paciente.apellido, "Pérez")
        self.assertEqual(paciente.dni, "12345678")

    def test_obtener_paciente(self):
        paciente_id, _ = self.service.registrar_paciente(
            "Ana", "Gómez", "87654321", "ana@mail.com", "1995-05-05", "2615554321"
        )
        paciente = self.service.obtener_paciente(paciente_id)
        self.assertIsNotNone(paciente)
        self.assertEqual(paciente.apellido, "Gómez")

if __name__ == "__main__":
    unittest.main()
