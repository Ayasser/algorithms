from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .views import get_factorial

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_factorial(self):
        print('\n\tfactorial test cases:')
        print('\t\ttest factorial should return 200 with correct value')
        request = self.factory.get('factorial?number=5')

        response = get_factorial(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), int)
        self.assertEqual(response.data, 120)

    def test_get_factorial_with_empty_param(self):
        print('\t\ttest factorial empty param should return 400')
        request = self.factory.get('factorial?number=')

        response = get_factorial(request)
        self.assertEqual(response.status_code, 400)

    def test_get_factorial_with_negative(self):
        print('\t\ttest factorial negative number param should return 400')
        request = self.factory.get('factorial?number=-12')

        response = get_factorial(request)
        self.assertEqual(response.status_code, 400)
    def test_get_factorial_with_string(self):
        print('\t\ttest factorial string param should return 400')
        request = self.factory.get('factorial?number=ww')

        response = get_factorial(request)
        self.assertEqual(response.status_code, 400)