from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book
# Create your tests here.
class BookListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('book-list')
        self.book = Book.objects.create_book(title = "When did you see her last?", author = "Kelvin Sibuta")
    def test_Book_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        books = [book['title'] for book in response.data]
        self.assertIn('When did you see her last?', title)from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book
# Create your tests here.
class BookListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('book-list')
        self.book = Book.objects.create_book(title = "When did you see her last?", author = "Kelvin Sibuta")
    def test_Book_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        books = [book['title'] for book in response.data]
        self.assertIn('When did you see her last?', title)
        self.assertTrue(len(title) != 0)

class BookRetrieveTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('book-list')
        self.book = Book.objects.create_book(title = "When did you see her last?", author = "Kelvin Sibuta")
    def test_Book_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        books = [book['title'] for book in response.data]
        self.assertIn('When did you see her last?', title)
        self.assertTrue(len(title) != 0)