from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .views import get_fibonacci

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_fibonacci(self):
        print('\n\tfibonacci test cases:')
        print('\t\ttest fibonacci should return 200 with correct value')
        request = self.factory.get('fibonacci?number=12')

        response = get_fibonacci(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), int)
        self.assertEqual(response.data, 144)

    def test_get_fibonacci_with_empty_param(self):
        print('\t\ttest fibonacci empty param should return 400')
        request = self.factory.get('fibonacci?number=')

        response = get_fibonacci(request)
        self.assertEqual(response.status_code, 400)

    def test_get_fibonacci_with_negative(self):
        print('\t\ttest fibonacci negative number param should return 400')
        request = self.factory.get('fibonacci?number=-12')

        response = get_fibonacci(request)
        self.assertEqual(response.status_code, 400)
    def test_get_fibonacci_with_string(self):
        print('\t\ttest fibonacci string param should return 400')
        request = self.factory.get('fibonacci?number=ww')

        response = get_fibonacci(request)
        self.assertEqual(response.status_code, 400)