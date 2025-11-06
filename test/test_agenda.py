from datetime import date
import os
import unittest
from app.models import Agenda, Recepcionista
from app.services import AgendaService, RecepcionistaService
from app import create_app, db

class TestAgenda(unittest.TestCase):
    # Tests para la entidad Agenda (crear, leer, listar)
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

    def test_create_agenda(self):
        # Crear una agenda y verificar campos
        agenda = self._create_agenda(fecha=date(2024, 12, 20))
        
        self.assertIsNotNone(agenda.id)
        self.assertEqual(agenda.fecha, date(2024, 12, 20))
        self.assertEqual(agenda.recepcionista_id, 1)

    def _create_recepcionista(self):
        # Helper: crear una recepcionista persistida
        recepcionista = Recepcionista(
            nombre="Ana",
            email="ana@mail.com",
        )
        recepcionista = RecepcionistaService.create(recepcionista)
        return recepcionista

    def test_get_agenda_by_id(self):
        # Obtener agenda por id
        agenda = self._create_agenda(fecha=date(2024, 12, 20))

        fetched_agenda = AgendaService.get_by_id(agenda.id)
        self.assertIsNotNone(fetched_agenda)
        self.assertEqual(fetched_agenda.fecha, date(2024, 12, 20))

    def test_read_all_agendas(self):
        # Listar todas las agendas
        agenda1 = self._create_agenda(fecha=date(2024, 12, 20))
        agenda2 = self._create_agenda(fecha=date(2024, 12, 21))

        agendas = AgendaService.read_all()
        self.assertEqual(len(agendas), 2)


    def _create_agenda(self, fecha=date(2024, 12, 20), recepcionista=None):
        # Helper: crear y persistir una agenda
        if recepcionista is None:
            recepcionista = self._create_recepcionista()
        self.assertIsNotNone(recepcionista.id)
        agenda = Agenda(
            fecha=fecha,
            recepcionista=recepcionista
        )
        return AgendaService.create(agenda)


if __name__ == "__main__":
    unittest.main()
