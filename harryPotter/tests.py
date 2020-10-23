from django.test import TestCase
from rest_framework import status

# Create your tests here.
class HarryPotterTestCase(TestCase):   
   
    """
    TEST SORTING HAT
    Returns a house from Hogwarts ('Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff')
    """
    def test_sorting_hat(self):
        response = self.client.get('/sortingHat/')
        self.assertIn(response.data, ['Gryffindor', 'Ravenclaw', 'Slytherin', 'Hufflepuff'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    """
    TEST CHARACTERS
    Returns the characters from Harry Potter
    """
    def test_characters(self):
        response = self.client.get('/characters/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    """
    TEST CHARACTERS WITH NAME
    Returns a character with a given name
    """
    def test_character_name(self):
        response = self.client.get('/characters/', {'name':'Harry Potter'})
        self.assertEqual(response.data[0]['name'], 'Harry Potter')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    """
    TEST CHARACTERS WITH HOUSE
    Returns a character from 'Slytherin'
    """
    def test_character_house(self):
        response = self.client.get('/characters/', {'house':'Slytherin'})
        self.assertEqual(response.data[0]['house'], 'Slytherin')
        self.assertEqual(response.status_code, status.HTTP_200_OK)