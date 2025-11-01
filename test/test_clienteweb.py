import os
import unittest
from flask import current_app
from app import create_app, db


class ClienteWebTestCase(unittest.TestCase):

    def setUp(self):
        # Usar configuración de testing como el resto de tests
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_endpoint(self):
        res = self.client.get('/api/v1/')
        self.assertEqual(res.status_code, 200)
        self.assertIsNotNone(res.json)
        self.assertIn('message', res.json)
        self.assertEqual(res.json['message'], 'ok')

    def test_pagina_no_encontrada(self):
        res = self.client.get('/ruta-que-no-existe')
        self.assertEqual(res.status_code, 404)


if __name__ == '__main__':
    unittest.main()
