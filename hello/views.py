from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

"""
GET
Returns Hello World message
"""
@api_view(['GET'])
def hello_world(request):
    return Response(data='Hello Wizard!!', status=status.HTTP_200_OK)