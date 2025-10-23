import unittest
from app.models import Agenda, Turno
from app.services import AgendaService

class TestAgenda(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_and_get_agenda(self):
        agenda_data = {"recepcionista_id": 1}
        agenda = self.repo.add_agenda(agenda_data)
        fetched = self.repo.get_agenda(agenda.recepcionista_id)
        self.assertEqual(fetched.recepcionista_id, 1)
        self.assertEqual(fetched.turnos, [])

    def test_list_agendas(self):
        self.repo.add_agenda({"recepcionista_id": 1})
        self.repo.add_agenda({"recepcionista_id": 2})
        agendas = self.repo.list_agendas()
        self.assertEqual(len(agendas), 2)
        self.assertEqual(agendas[0].recepcionista_id, 1)
        self.assertEqual(agendas[1].recepcionista_id, 2)

    def test_delete_agenda(self):
        agenda = self.repo.add_agenda({"recepcionista_id": 3})
        result = self.repo.delete_agenda(agenda.recepcionista_id)
        self.assertTrue(result)
        self.assertIsNone(self.repo.get_agenda(agenda.recepcionista_id))

    def test_update_agenda(self):
        agenda = self.repo.add_agenda({"recepcionista_id": 4})
        updated = self.repo.update_agenda(agenda.recepcionista_id, {"recepcionista_id": 5})
        self.assertEqual(updated.recepcionista_id, 5)

    def test_agregar_y_eliminar_turno(self):
        agenda = self.repo.add_agenda({"recepcionista_id": 6})
        turno = Turno(id=1, paciente_id=1, fecha="2025-10-17")
        agenda.agregar_turno(turno)
        self.assertEqual(len(agenda.turnos), 1)
        self.assertEqual(agenda.turnos[0].id, 1)
        agenda.eliminar_turno(turno)
        self.assertEqual(len(agenda.turnos), 0)

if __name__ == "__main__":
    unittest.main()
