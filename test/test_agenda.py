import unittest
from flask import current_app
from app import create_app
from app.models.agenda import Agenda
from app.models.turno import Turno
from datetime import date, time
import os

class AgendaTestCase(unittest.TestCase):

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

    def test_agenda_creacion(self):
        """Prueba que la agenda se cree con lista de turnos vacía"""
        agenda = Agenda(recepcionista_id=1)
        self.assertEqual(agenda.recepcionista_id, 1)
        self.assertEqual(len(agenda.turnos), 0)

    def test_agregar_turno(self):
        """Prueba agregar un turno a la agenda"""
        agenda = Agenda(recepcionista_id=1)
        turno = Turno(
            fecha=date(2025, 8, 21),
            hora=time(10, 30),
            estado="disponible"
        )

        agenda.agregar_turno(turno)

        self.assertEqual(len(agenda.turnos), 1)
        self.assertEqual(agenda.turnos[0].estado, "disponible")

    def test_eliminar_turno(self):
        """Prueba eliminar un turno de la agenda"""
        agenda = Agenda(recepcionista_id=1)
        turno = Turno(
            fecha=date(2025, 8, 21),
            hora=time(11, 0),
            estado="disponible"
        )
        agenda.agregar_turno(turno)

        self.assertEqual(len(agenda.turnos), 1)  # antes de eliminar
        agenda.eliminar_turno(turno)

        self.assertEqual(len(agenda.turnos), 0)  # después de eliminar


if __name__ == '__main__':
    unittest.main()
