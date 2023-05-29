from django.db import models


class Article(models.Model):
    title = models.TextField('Назва', max_length=400)
    anons = models.TextField('Цитата', max_length=400)
    full_text = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'
