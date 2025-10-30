import os
import unittest
from flask import current_app
from app import create_app
from app.models import Recepcionista
from app.services import RecepcionistaService
from app import db
class RecepcionistaTestCase(unittest.TestCase):

    def setUp(self):
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
        self.assertIsNotNone(current_app)

    def test_registrar_recepcionista(self):
        recepcionista = self._create_recepcionista()
        self.assertIsNotNone(recepcionista.id)

    def _create_recepcionista(self):
        recepcionista = Recepcionista(
            nombre="Ana",
            email="ana@mail.com",
        )
        recepcionista = RecepcionistaService.create(recepcionista)
        return recepcionista

    def test_obtener_recepcionista(self):
        recepcionista = self._create_recepcionista()
        recepcionista = RecepcionistaService.get_by_id(recepcionista.id)
        self.assertIsNotNone(recepcionista)
        self.assertEqual(recepcionista.nombre, "Ana")

    def test_actualizar_recepcionista(self):
        recepcionista = self._create_recepcionista()
        recepcionista.nombre = "Maria"
        recepcionista.email = "maria@mail.com"
        result = RecepcionistaService.update(recepcionista)
        self.assertTrue(result)
        self.assertEqual(recepcionista.nombre, "Maria")
        self.assertEqual(recepcionista.email, "maria@mail.com")


    def test_eliminar_recepcionista(self):
        recepcionista = self._create_recepcionista()
        result = RecepcionistaService.delete(recepcionista.id)
        self.assertTrue(result)
        recepcionista = RecepcionistaService.get_by_id(recepcionista.id)
        self.assertIsNone(recepcionista)


if __name__ == '__main__':
    unittest.main()
