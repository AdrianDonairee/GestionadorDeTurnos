import unittest
from app.services.recepcionista_service import RecepcionistaService
from app.repositories.recepcionista_repository import RecepcionistaRepository

class TestRecepcionistaService(unittest.TestCase):
    def setUp(self):
        self.repository = RecepcionistaRepository()
        self.service = RecepcionistaService(self.repository)

    def test_registrar_recepcionista(self):
        recepcionista_id, recepcionista = self.service.registrar_recepcionista(
            "Laura", "laura@mail.com"
        )
        self.assertEqual(recepcionista_id, 1)
        self.assertEqual(recepcionista.nombre, "Laura")
        self.assertEqual(recepcionista.email, "laura@mail.com")

    def test_obtener_recepcionista(self):
        recepcionista_id, _ = self.service.registrar_recepcionista(
            "Pedro", "pedro@mail.com"
        )
        recepcionista = self.service.obtener_recepcionista(recepcionista_id)
        self.assertIsNotNone(recepcionista)
        self.assertEqual(recepcionista.nombre, "Pedro")

if __name__ == "__main__":
    unittest.main()
