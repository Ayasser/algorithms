from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import time
# def fibonacci(number): 
#     fibonacci_of_zero = 0
#     fibonacci_of_one = 1
#     if number == 0:
#         return fibonacci_of_zero 
#     elif number == 1: 
#         return fibonacci_of_one 
#     else:
#         for i in range(2,int(number)+1):
#             total = fibonacci_of_zero + fibonacci_of_one 
#             fibonacci_of_zero = fibonacci_of_one 
#             fibonacci_of_one = total 
#         return fibonacci_of_one 

def fibonacci(number): 
      
    fib = [[1, 1], [1, 0]] 
    if (number == 0): 
        return 0
    power(fib, number - 1) 
          
    return fib[0][0] 
      
def multiply(fib, matrix):      
    matrix_0_0 = (fib[0][0] * matrix[0][0] + fib[0][1] * matrix[1][0]) 
    matrix_0_1 = (fib[0][0] * matrix[0][1] + fib[0][1] * matrix[1][1]) 
    matrix_1_0 = (fib[1][0] * matrix[0][0] + fib[1][1] * matrix[1][0]) 
    matrix_1_1 = (fib[1][0] * matrix[0][1] + fib[1][1] * matrix[1][1]) 
      
    fib[0][0] = matrix_0_0 
    fib[0][1] = matrix_0_1 
    fib[1][0] = matrix_1_0 
    fib[1][1] = matrix_1_1
          
def power(fib, number): 
    if( number == 0 or number == 1): 
        return 1
    matrix = [[1, 1], [1, 0]]; 
          
    power(fib, number // 2) 
    multiply(fib, fib) 
          
    if (number % 2 != 0): 
        multiply(fib, matrix) 

@api_view(['GET'])
def get_fibonacci(request):

    if request.method == 'GET':
        start_time = time.time()
        number = request.query_params.get('number')
        if number is None:
            return Response("Please send number", status=status.HTTP_400_BAD_REQUEST)

        if ( not number.isnumeric() ) or ( len(number)==0 ) or ( not (float(number) % 1 == 0) ) or ( float(number) < 0 ):
            return Response("Number must be postive integer", status=status.HTTP_400_BAD_REQUEST)

        try:
            result = fibonacci(int(number))
            duration = time.time() - start_time
            print('\033[93m','\tResponse time:', float(duration * 1000))
            print('\n')
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)
