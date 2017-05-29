# -*- coding: utf-8 -*-
from django.db import models
from flavors.models import Flavor


# Create your models here.
class Order(models.Model):
    flavor = models.ForeignKey(Flavor, verbose_name="Букет")
    name = models.CharField("имя", max_length=50)
    phone = models.CharField("телефон", max_length=50)
    adress = models.CharField('адрес', max_length=300)
    date = models.DateTimeField("дата", auto_now_add=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["flavor"]

    def __str__(self):
        return self.flavor
