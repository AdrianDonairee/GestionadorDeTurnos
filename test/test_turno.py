import unittest
from flask import current_app
from app import create_app
from app.models import Turno
from app.services import TurnoService
from datetime import date, time
import os

class TurnoTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        """Verifica que la app se haya creado bien"""
        self.assertIsNotNone(current_app)

    def test_creacion_turno(self):
        """Prueba que se cree un turno correctamente"""
        turno = Turno(
            fecha=date(2025, 8, 21),
            hora=time(10, 30),
            estado="disponible"
        )
        TurnoService.create(turno)
        self.assertEqual(turno.fecha, date(2025, 8, 21))
        self.assertEqual(turno.hora, time(10, 30))
        self.assertEqual(turno.estado, "disponible")

    def test_asignar_cliente(self):
        """Prueba que un turno pueda asignarse a un cliente"""
        turno = Turno(
            fecha=date(2025, 8, 21),
            hora=time(10, 30)
        )
        turno.asignar_cliente()
        self.assertEqual(turno.estado, "reservado")

    def test_liberar_turno(self):
        """Prueba que un turno pueda liberarse"""
        turno = Turno(
            fecha=date(2025, 8, 21),
            hora=time(10, 30),
            estado="reservado"
        )
        turno.liberar_turno()
        self.assertEqual(turno.estado, "disponible")


if __name__ == '__main__':
    unittest.main()