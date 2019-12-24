from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import time

def ackermann(m,n):
    if m == 0:
        result = n + 1
    elif n == 0:
        result = ackermann(m-1, 1)
    else:
        result = ackermann(m-1, ackermann(m, n-1))
    return result

@api_view(['GET'])
def get_ackermann(request):

    if request.method == 'GET':
        start_time = time.time()

        first_number = request.query_params.get('firstnumber')
        second_number = request.query_params.get('secondnumber')
        
        if first_number is None or second_number is None:
            return Response("Please send first and second number", status=status.HTTP_400_BAD_REQUEST)

        if ( not first_number.isnumeric() ) or ( len(first_number)==0 ) or \
                ( not (float(first_number) % 1 == 0) ) or  ( float(first_number) < 0 ):
            return Response("first number must be postive integer", status=status.HTTP_400_BAD_REQUEST)

        if ( not second_number.isnumeric() ) or ( len(second_number)==0 ) or \
                ( not (float(second_number) % 1 == 0) ) or  ( float(second_number) < 0 ):
            return Response("second number must be postive integer", status=status.HTTP_400_BAD_REQUEST)

        try:
            result = ackermann(int(first_number), int(second_number))
            duration = time.time() - start_time
            print('\033[93m','\tResponse time:', float(duration * 1000))
            print('\n')
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
