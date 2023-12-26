from django.test import TestCase
from django.urls import reverse
from .models import Article
from django.core.files.uploadedfile import SimpleUploadedFile

class NewsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Створення тестових статей
        number_of_articles = 5
        for article_id in range(number_of_articles):
            Article.objects.create(
                title=f'Article {article_id}',
                full_text='This is a test article'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/news.html')


    def test_lists_all_articles(self):
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['news_arr']) == 5)


class ArticleDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Створення тестової статті з усіма необхідними полями
        cls.article = Article.objects.create(
            title='Test Article',
            anons='Test Anons',
            full_text='This is a full text of the article. It is quite long.',
            photolink_1=SimpleUploadedFile('test_photo1.jpg', content=b'', content_type='image/jpeg'),
            photolink_2=SimpleUploadedFile('test_photo2.jpg', content=b'', content_type='image/jpeg')
        )

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('news-detail', args=[str(self.article.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/example.html')

    def test_context_data(self):
        response = self.client.get(reverse('news-detail', args=[str(self.article.id)]))
        self.assertTrue('first_half_text' in response.context)
        self.assertTrue('second_half_text' in response.context)
        full_text = self.article.full_text
        self.assertEqual(response.context['first_half_text'], full_text[:len(full_text)//2])
        self.assertEqual(response.context['second_half_text'], full_text[len(full_text)//2:])
