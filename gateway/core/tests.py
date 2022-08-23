from django.test import TestCase, Client
import requests

class LoginTestCase(TestCase):
    client = Client()

    def test_login(self):
        response = self.client.post('/login', {'username': 'tabarochristian', 'password': 'Kinshasa-2021'})
        self.assertEqual(response.status_code, 200)

class ProductServiceTestCase(TestCase):
    service_url = "http://localhost:7000"
    def test_crudl_product(self):
        response = requests.post(f'{self.service_url}/products/', {"name": "Product.0001"})
        id = response.json().get('id')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(requests.get(f'{self.service_url}/products/').status_code, 200)
        self.assertEqual(requests.get(f'{self.service_url}/products/{id}/').status_code, 200)
        self.assertEqual(requests.put(f'{self.service_url}/products/{id}/', {"name": "Product.0001"}).status_code, 200)
        self.assertEqual(requests.delete(f'{self.service_url}/products/{id}/').status_code, 204)

class OrderServiceTestCase(TestCase):
    service_url = "http://localhost:7001"

    def test_crudl_product(self):
        response = requests.post(f'{self.service_url}/orders/', {"product_id": 1})
        id = response.json().get('id')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(requests.get(f'{self.service_url}/orders/').status_code, 200)
        self.assertEqual(requests.get(f'{self.service_url}/orders/{id}/').status_code, 200)
        self.assertEqual(requests.put(f'{self.service_url}/orders/{id}/', {"product_id": 2}).status_code, 200)
        self.assertEqual(requests.delete(f'{self.service_url}/orders/{id}/').status_code, 204)

