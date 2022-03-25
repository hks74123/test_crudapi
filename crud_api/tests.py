from django.contrib.auth.models import User
from django.urls import include, path, resolve, reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class Student_data_testing(APITestCase):
    student_ulr = reverse('allstudents')
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin', password='admin')
        self.client = APIClient()
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.refresh.access_token}')
    
    def test_get_customers_authenticated(self):
        response = self.client.get(self.student_ulr)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_customers_un_authenticated(self):
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get(self.student_ulr)
        self.assertEquals(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_customer_authenticated(self):
        data = {
            "name":"Piyush",
            "roll":"57",
            "city":"lucknow"
        }
        response = self.client.post(self.student_ulr, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
         

    

