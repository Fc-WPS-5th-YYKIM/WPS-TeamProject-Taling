from django.contrib.auth import get_user_model
from django.test import TestCase, LiveServerTestCase

# Create your tests here.
from rest_framework import status
from rest_framework.reverse import reverse

User = get_user_model()


class MyUserTestCase(TestCase):
    def test_user_create(self):
        data = {'username': 'admin123', 'password': 'qwer1234', \
                'email': 'admin@admin.com', 'phone': '010-7242-2659'}
        url = reverse('member:user-list-or-create')
        response = self.client.post(url, data=data)
        self.assertEqual(User.objects.count(),1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.data)

    def test_user_delete(self):
        pass