from django.test import TestCase, Client
from django.urls import reverse
from news.models import Article

class MainViewsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Створення тестових статей для перевірки відображення на головній сторінці
        for i in range(5):
            Article.objects.create(
                title=f'Test Article {i+1}',
                full_text=f'This is a test article {i+1}.'
            )

    def test_index_view(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/index.html')
        # Перевірка, що статті передаються у контексті
        self.assertTrue('photo1' in response.context)
        self.assertTrue('photo2' in response.context)
        self.assertTrue('photo3' in response.context)
        self.assertTrue('photo4' in response.context)
        self.assertTrue('photo5' in response.context)

    def test_drivers_view(self):
        client = Client()
        response = client.get(reverse('drivers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/drivers.html')

    def test_schedule_view(self):
        client = Client()
        response = client.get(reverse('schedule'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/schedule.html')

    def test_standings_view(self):
        client = Client()
        response = client.get(reverse('standings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/standings.html')

    def test_teams_view(self):
        client = Client()
        response = client.get(reverse('teams'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/teams.html')
