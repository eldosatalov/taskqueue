from django.db import models


class Task(models.Model):
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    name = models.CharField('Название задачи', max_length=512)  # Можно и сдеать text field
    start_date = models.DateTimeField('Дата создания', null=True)
    end_date = models.DateTimeField('Дата создания', null=True)
    success = models.BooleanField('Задача выполнена', null=True)

    def __str__(self):
        return str(self.name)

