from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from rest_framework import status


class MenuViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.token = Token.objects.create(user=self.user)

        Menu.objects.create(Title="Pizza", Price=12.50, Inventory=10)
        Menu.objects.create(Title="Burger", Price=8.50, Inventory=15)
        Menu.objects.create(Title="Pasta", Price=10.00, Inventory=8)

    def test_getall(self):
        client = APIClient()

        client.credentials(
            HTTP_AUTHORIZATION="Token " + self.token.key
        )

        response = client.get('/restaurant/menu/')

        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)