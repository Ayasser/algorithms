from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import math
import time

# Create your views here.
@api_view(['GET'])
def get_factorial(request):

    if request.method == 'GET':
        start_time = time.time()

        number = request.query_params.get('number')
        if number is None:
            return Response("Please send number", status=status.HTTP_400_BAD_REQUEST)

        if ( not number.isnumeric() ) or ( len(number)==0 ) or ( not (float(number) % 1 == 0) ) or ( float(number) < 0 ):
            return Response("Number must be postive integer", status=status.HTTP_400_BAD_REQUEST)

        try:
            result = math.factorial(int(number))
            duration = time.time() - start_time
            print('\033[93m','\tResponse time:', float(duration * 1000))
            print('\n')
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

