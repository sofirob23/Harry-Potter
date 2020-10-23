from django.test import TestCase
from rest_framework import status

# Create your tests here.
class HelloTestCase(TestCase):
    
    """
    TEST HELLO
    Expected Result 'Hello Wizard!!'
    """
    def test_hello(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.data, 'Hello Wizard!!')
        self.assertEqual(response.status_code, status.HTTP_200_OK)