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
        db.create_all()

    def tearDown(self):
       
        db.session.remove()
        db.drop_all()
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
        TurnoService.asignar_cliente( turno, "reservado")
        TurnoService.update(turno)
        self.assertEqual(turno.estado, "reservado")

    def test_liberar_turno(self):
        """Prueba que un turno pueda liberarse"""
        turno = Turno(
            fecha=date(2025, 8, 21),
            hora=time(10, 30),
            estado="reservado"
        )
        TurnoService.asignar_cliente( turno, "disponible")
        TurnoService.update(turno)
        
        self.assertEqual(turno.estado, "disponible")
    
    def test_obtener_turno_por_id(self):
        """Prueba que un turno pueda obtenerse por su ID"""
        turno = Turno(
            fecha=date(2025, 8, 21),
            hora=time(10, 30)
        )
        TurnoService.create(turno)
        turno_obtenido = TurnoService.get_by_id(turno.id)
        self.assertIsNotNone(turno_obtenido)
        self.assertEqual(turno_obtenido.id, turno.id)  
    
    def test_obtenertodos_los_turnos(self):
        """Prueba que todos los turnos puedan obtenerse"""
        turno1 = Turno(
            fecha=date(2025, 8, 21),
            hora=time(10, 30)
        )
        turno2 = Turno(
            fecha=date(2025, 8, 22),
            hora=time(11, 30)
        )
        TurnoService.create(turno1)
        TurnoService.create(turno2)
        turnos = TurnoService.read_all()
        self.assertGreaterEqual(len(turnos), 2)

    def test_borrar_turno(self):
        """Prueba que un turno pueda borrarse"""
        turno = Turno(
            fecha=date(2025, 8, 21),
            hora=time(10, 30)
        )
        TurnoService.create(turno)
        turno_id = turno.id
        TurnoService.delete(turno_id)
        turno_borrado = TurnoService.get_by_id(turno_id)
        self.assertIsNone(turno_borrado)

    def _create_agenda(self, fecha=date(2024, 12, 20), recepcionista=None):
        if recepcionista is None:
            recepcionista = self._create_recepcionista()
        self.assertIsNotNone(recepcionista.id)
        agenda = Agenda(
            fecha=fecha,
            recepcionista=recepcionista
        )
        return AgendaService.create(agenda)

if __name__ == '__main__':
    unittest.main()