from django.db import models


class Contest(models.Model):
    title = models.CharField('Название', max_length=20)
    description = models.CharField('Описание')
    price = models.IntegerField(
        'Цена', help_text='Рекомендованная розничная цена'
    )
    comment = models.CharField('Комментарий')
