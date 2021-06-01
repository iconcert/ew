from django.db import models


class Page(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    body = models.TextField('Описание')
    image = models.ImageField(upload_to='images/pages/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.title