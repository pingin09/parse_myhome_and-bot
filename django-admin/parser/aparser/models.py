from django.db import models


class last_Requests(models.Model):
    id_member = models.PositiveIntegerField(verbose_name='ID пользователя')
    city = models.TextField(verbose_name='Город')
    types_requests = models.TextField(verbose_name='Тип жилья')
    count_rooms = models.PositiveSmallIntegerField(verbose_name='Количество комнат')
    min_price = models.PositiveIntegerField(verbose_name='Минимальный прайс')
    max_price = models.PositiveIntegerField(verbose_name='Максимальный прайс')
    owner = models.BooleanField(verbose_name='Собственник')

    def __str__(self):
        return f'#'
