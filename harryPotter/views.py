from django.shortcuts import render
from dotenv import load_dotenv
import json
import os
import requests
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status


"""
GET HOUSE
Returns a random hogwarts house. Using https://www.potterapi.com/
"""
@api_view(['GET'])
def get_house(request):
    load_dotenv()

    url = os.getenv("URL") + 'sortingHat/'
    response = requests.get(url)

    if response.status_code == 200:
        return Response(data=json.loads(response.text), status=status.HTTP_200_OK)
    else:
        return Response(data=json.loads(response.text), status=response.status_code)


"""
GET CHARACTER
Returns a harry potter character with given parameters using a key to the API.
"""
@api_view(['GET'])
def get_character(request):
    load_dotenv()

    params = request.query_params.dict()
    params['key'] = os.getenv("KEY")
    url = os.getenv("URL") + 'characters/'

    response = requests.get(url, params)

    if response.status_code == 200:
        return Response(data=json.loads(response.text), status=status.HTTP_200_OK)
    else:
        return Response(data=json.loads(response.text), status=response.status_code)