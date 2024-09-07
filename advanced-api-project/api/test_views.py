from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author

class UserCreationTestCase(APITestCase):
    def setUp(self):
        """This block of code creates a user"""
        self.user = User.objects.create_user(username='kssibuta', password='password')
        self.client = APIClient()
        
    def test_create_book_authenticated(self):
    """Tests if the client can create a book"""
        self.client.login(username='kssibuta', password='password')

        url = reverse('book-create')
        data = {
            'title': 'When did you see her last?',
            'author': 'Sibuta',
            'publication_year': 1996
        }
        response = self.client.post(url, data, format='json')

        """The code below check that the response is 201 Created"""
        self.assertEqual(response.status_code, 201)
        
        """""The code below check that the book was Created"""""
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'When did you see her last?')

    def test_create_book_unauthenticated(self):
        """This code restricts unathorized users from creating a book"""

        url = reverse('book-create')
        data = {
            'title': 'When did you see her last?',
            'author': 'Sibuta',
            'publication_year': 1996}
        response = self.client.post(url, data, format='json')

        """ The code below checks that the response is 401 Unauthorized"""
        
        self.assertEqual(response.status_code, 401)


class BookRetrievalTestCase(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(title='When did you see her last?', author='Sibuta', publication_year=1996)
        self.client = APIClient()

    def test_get_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')

        """The code below checks that the response was successful, 200 OK"""
        self.assertEqual(response.status_code, 200)
        """The code  below checks that the length of response data is 1"""
        self.assertEqual(len(response.data), 1)
        
        self.assertEqual(response.data[0]['title'], 'When did you see her last?')

    def test_get_book_detail(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url, format='json')

        """The code below checks that the response is 200 OK"""
        self.assertEqual(response.status_code, 200)
        
        """The code below checks that the response contains correct book details"""
        self.assertEqual(response.data['title'], 'When did you see her last?')

class BookUpdateTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='simiyu', password='password')
        self.book = Book.objects.create(title='When the sun shines', author='Junior', publication_year=2014)
        self.client = APIClient()

    def test_update_book_authenticated(self):
        self.client.login(username='simiyu', password='password')
        url = reverse('book-update', args=[self.book.id])
        data = {
            'title': 'Recipes',
            'author': 'HWK',
            'publication_year': 2016
        }
        response = self.client.put(url, data, format='json')

        """The code below checks that the response is 200 OK"""
        self.assertEqual(response.status_code, 200)
        
        """Checks that the book was updated"""
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Recipes')

    def test_update_book_unauthenticated(self):
        url = reverse('book-update', args=[self.book.id])
        data = {
            'title': 'Recipes',
            'author': 'HWK',
            'publication_year': 2016
        }
        response = self.client.put(url, data, format='json')

        """The code below checks if the response is 401 Unauthorized"""
        self.assertEqual(response.status_code, 401)

class BookDeletionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='makona', password='password')
        self.book = Book.objects.create(title='Deleted book', author='John', publication_year=2013)
        self.client = APIClient()

"""The code below tests if the user is authorized to delete a book"""
    def test_delete_book_authenticated(self):
        self.client.login(username='makona', password='password')
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url, format='json')

        """The code below checks that the response is 204 No Content"""
        self.assertEqual(response.status_code, 204)
        
        """ The code below confirms that the book was deleted"""
        self.assertEqual(Book.objects.count(), 0)

    """The code below tests if the user can delete a book"""
    def test_delete_book_unauthenticated(self):
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url, format='json')

    """The code below checks that the user is unathorized to delete the book returning a response 401 Unauthorized""""
        self.assertEqual(response.status_code, 401)

class BookFilterSearchOrderTestCase(APITestCase):
    def setUp(self):
        Book.objects.create(title='When did you see her last?', author='Sibuta', publication_year=1996)
        Book.objects.create(title='Recipes', author='HWK', publication_year=2016)
        Book.objects.create(title='When the sun shines', author='Junior', publication_year=2014)
        self.client = APIClient()

    def test_filter_by_author(self):
        url = reverse('book-list')
        response = self.client.get(url, {'author': 'Sibuta'}, format='json')

        """Check that the response is 200 OK"""

        self.assertEqual(response.status_code, 200)

        """" The code below checks that only the books by Sibuta are returned"""
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Sibuta')

    def test_search_title(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Recipes'}, format='json')

        """The code below checks that the response is 200 OK"""
        self.assertEqual(response.status_code, 200)

        """The code below checks if the correct book is returned"""
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Recipes')

    def test_ordering_by_publication_year(self):
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'}, format='json')

        """The code below checks that the response is 200 OK"""
        self.assertEqual(response.status_code, 200)

        """The code below verifies that books are ordered by publication_year"""
        publication_years = [book['publication_year'] for book in response.data]
        self.assertEqual(publication_years, sorted(publication_years))

class BookPermissionsTestCase(APITestCase):
    def setUp(self):
        self.book = Book.objects.create(title='New Beginnings', author='Machache', publication_year=2023)
        self.client = APIClient()

    """Unauthenticated users should only have a read-only access"""
    def test_read_only_access_unauthenticated(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

        """Unauthenticated users are restricted from creating a book"""
        url = reverse('book-create')
        data = {'title': 'Dreaming of Farlands', 'author': 'Faith', 'publication_year': 2020}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 401)

    """The code below gives full access previledges to the user"""
    def test_full_access_authenticated(self):
        self.user = User.objects.create_user(username='Sibuta', password='password')
        self.client.login(username='Sibuta', password='password')
        
        url = reverse('book-create')
        data = {'title': 'Sunrise', 'author': 'Sibuta', 'publication_year': 2024}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)