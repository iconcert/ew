from django.db import models


class New(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    body = models.TextField('Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='images/news/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

    def __str__(self):
        return self.title