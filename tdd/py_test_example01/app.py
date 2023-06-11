import requests
import unittest
import json 

class TestApi(unittest.TestCase):

    def test_create(self):
        url = 'http://127.0.0.1:5000/users/create'

        payload = {
            "name": "Derick",
            "age": "45",
            "address": "Rua Boston 137"
        }

        headers = {
            "Content-Type": "application/json"
        }

        # creating request post
        response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
        
        data = response.json()[0]

        # print(data)
        self.assertEqual(data['name'], payload['name'])
        self.assertEqual(data['age'], payload['age'])
        self.assertEqual(data['address'], payload['address'])

        id = data['id']

        payload = {
            "name": "Mario",
            "age": "40",
            "address": "Rua Nova Jersey 107"
        }

        url = f'http://127.0.0.1:5000/users/update/{id}/edit'

        response = requests.request("PUT", url, headers=headers, data=json.dumps(payload))

        data = response.json()

        # print(data)
