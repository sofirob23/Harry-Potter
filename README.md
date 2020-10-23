# Harry Potter API

This API consists on 3 endpoints. Using the external API https://www.potterapi.com

# About the Application

This Application was developed in Python Django by Sofia Robles Sandoval

### Requirements

- Django==3.1.2
- djangorestframework==3.12.1
- python-dotenv==0.10.3
- requests==2.24.0

To install requirements run the following command: `pip install -r requirements.txt`

### How To Run

Make sure to have the requirements installed before you run the application. 
Go to harry_potter_api directory and run the following command: `python manage.py runserver`

### Endpoints

#### `/hello/`
Make a GET request to [localhost:8000/hello/](localhost:8000/hello/)
You should receive a Hello Message

#### `/sortingHat/`
Make a GET request to [localhost:8000/sortingHat/](localhost:8000/sortingHat/)
You should receive a random Hogwarts house (Gryffindor, Ravenclaw, Slytherin or Hufflepuff).

#### `/characters/`
Make a GET request to [localhost:8000/characters/](localhost:8000/characters/)
You should receive a character based on one of the given parameters.

- name		
- house
- patronus		
- species
- bloodStatus	
- role		
- school		
- deathEater		
- dumbledoresArmy		
- orderOfThePhoenix		
- ministryOfMagic		
- alias		
- wand		
- boggart		
- animagus	

For more detail go to [Character Routes](https://www.potterapi.com/)


### Project Structure

#### `harry_potter_api`

Contains the settings for the application. In the urls.py you can find the different
for the existing endpoints.

#### `harryPotter`

This directory contains the endpoints related to the Harry Potter API.
In 'views.py' you can find the code for the different endpoints. 
In 'tests.py' you can find the test cases for the Harry Potter endpoints. 

#### `hello`

This directory contains the Hello World endpoint.
In 'views.py' you can find the code for the Hello World endpoint
In 'tests.py' you can find the test case for the endpoint.

### Testing

To run the test cases you should execute: `python manage.py test`.

### More Information

For more information About the API go to
[Harry Potter API](https://www.potterapi.com/)