from django.db import models

class Task(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=128,
    )
    desc = models.CharField(
        verbose_name='Описание',
        max_length=128,
    )
    completed = models.BooleanField(
        verbose_name='Выполнен',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title