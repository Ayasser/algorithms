from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .views import get_ackermann

class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_ackermann(self):
        print('\n\tackermann test cases:')
        print('\t\ttest ackermann should return 200 with correct value')
        request = self.factory.get('ackermann?firstnumber=3&secondnumber=3')

        response = get_ackermann(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.data), int)
        self.assertEqual(response.data, 61)

    def test_get_ackermann_with_empty_first_param(self):
        print('\t\ttest ackermann empty first param should return 400')
        request = self.factory.get('ackermann?first_number=&secondnumber=2')

        response = get_ackermann(request)
        self.assertEqual(response.status_code, 400)

    def test_get_ackermann_with_empty_second_param(self):
        print('\t\ttest ackermann empty second param should return 400')
        request = self.factory.get('ackermann?first_number=3&secondnumber=')

        response = get_ackermann(request)
        self.assertEqual(response.status_code, 400)

    def test_get_ackermann_with_first_number_negative(self):
        print('\t\ttest ackermann negative firstnumber param should return 400')
        request = self.factory.get('ackermann?first_number=-123&secondnumber=5')

        response = get_ackermann(request)
        self.assertEqual(response.status_code, 400)

    def test_get_ackermann_with_second_number_negative(self):
        print('\t\ttest ackermann negative secondnumber param should return 400')
        request = self.factory.get('ackermann?first_number=3&secondnumber=-5')

        response = get_ackermann(request)
        self.assertEqual(response.status_code, 400)

    def test_get_ackermann_with_first_number_string(self):
        print('\t\ttest ackermann string first param should return 400')
        request = self.factory.get('ackermann?first_number=ww&secondnumber=3')

        response = get_ackermann(request)
        self.assertEqual(response.status_code, 400)
    
    def test_get_ackermann_with_second_number_string(self):
        print('\t\ttest ackermann string second param should return 400')
        request = self.factory.get('ackermann?first_number=3&secondnumber=ww')

        response = get_ackermann(request)
        self.assertEqual(response.status_code, 400)
