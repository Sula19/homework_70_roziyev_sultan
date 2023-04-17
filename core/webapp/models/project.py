from django.db import models


class Project(models.Model):
    start_date = models.DateField(
        null=False,
        blank=False,
        verbose_name='Дата начала'
    )
    expiration_date = models.DateField(
        blank=True,
        verbose_name='Дата окончания'
    )
    name = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
        verbose_name='Описание'
    )

    def __str__(self):
        return f'{self.name} - {self.description}'
