import unittest
from flask import current_app
from app import create_app, db
from sqlalchemy import text
import os

class DbTestCase(unittest.TestCase):

    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        
        self.app_context.push()
        

    def tearDown(self):
        
        
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)

    def test_db_connection(self):
        from mysql.connector import (connection)

        cnx = connection.MySQLConnection(user='root', password='r00tgest10nad0r',
                                 host='127.0.0.1',
                                 database='test_turnos',
                                 port=3307)
        self.assertTrue(cnx.is_connected())                         
        cnx.close()
        

if __name__ == '__main__':
    unittest.main()