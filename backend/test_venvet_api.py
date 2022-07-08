import unittest
from flask_sqlalchemy import SQLAlchemy

from server import create_app
from models import setup_db, Users, Appointments
import json

class TestAppointmentApp(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'appointments_test'
        self.database_path = 'postgresql://{}:{}@{}/{}'.format('postgres','123456789', 'localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        self.new_appointment = {
            'name': 'Firulais',
            'pet': 'Perro',
            'date': '2022-03-04T23:28:56.782Z',
            'owner_id': 1
        }
        self.new_user = {
            'username': 'prueba',
            'password': 'Prueba1234'
        }
    def test_api_get(self):
        res = self.client().get('/api/')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_users_get(self):
        res = self.client().get('/api/users')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_citas_no_login(self):
        res = self.client().get('/api/citas')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertFalse(data["success"], True)

    def test_signup_user(self):
        res = self.client().post('/api/signup', json=self.new_user)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code,200)
        self.assertEqual(data["success"],True)
    def test_signup(self):
        res = self.client().post('/api/signup', json=self.new_user)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code,200)
        self.assertEqual(data["success"],True)
    
    def test_login_f(self):
        res0 = self.client().post('/api/signup', json=self.new_user)
        data0 = json.loads(res0.data)
        res1 = self.client().post('/api/login',json=self.new_user)
        data1 = json.loads(res1.data)
        self.assertEqual(res1.status_code,401)
        self.assertFalse(data1["success"])


    def test_logout_f(self):
        res = self.client().post('/api/signup', json=self.new_user)
        data = json.loads(res.data)
        res0 = self.client().post('/api/login',json = self.new_user)
        data0 = json.loads(res0.data)
        res1 = self.client().post('/api/logout', json=self.new_user)
        data1 = json.loads(res1.data) 

        self.assertEqual(res1.status_code, 401)
        self.assertFalse(data1['success'])

    def test_login_passwordfail(self):
        res0 = self.client().post('/api/signup',json=self.new_user)
        res = self.client().post('/api/login',json=self.new_user)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data["success"],False)
        self.assertEqual(data["message"], "Contraseña incorrecta")

    def test_signup_wrong_password_len(self):
        res = self.client().post('/api/signup',json={'username': 'prueba3', 'password': 'pass123'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "La contraseña debe tener minimo 8 caracteres")

    
    def test_signup_wrong_password_num(self):
        res = self.client().post('/api/signup',json={'username': 'prueba', 'password': 'Password'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "La contraseña debe tener mínimo un número")
    
    def test_signup_wrong_password_caps(self):
        res = self.client().post('/api/signup',json={'username': 'prueba', 'password': 'password1'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "La contraseña debe tener minimo una mayúscula")
    
    def test_signup_wrong_password_c0(self):
        res = self.client().post('/api/signup',json={'username': 'prueba', 'password': 'pass1'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "La contraseña debe tener minimo 8 caracteres")
    
    def test_signup_wrong_password_c1(self):
        res = self.client().post('/api/signup',json={'username': 'prueba', 'password': 'password'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "La contraseña debe tener minimo una mayúscula")

    def test_signup_wrong_password_c2(self):
        res = self.client().post('/api/signup',json={'username': 'prueba', 'password': 'pass'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "La contraseña debe tener minimo 8 caracteres")


        
      
       

       
if __name__ == '__main__':
    unittest.main()
