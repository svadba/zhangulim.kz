from django.db import models


# Create your models here.
class StarFlavor(models.Model):
    name = models.CharField('название', max_length=250)
    images = models.ImageField("фотография", upload_to="star/photos", default="", blank=True)

    class Meta:
        verbose_name = "Звездный букет"
        verbose_name_plural = "Звездная коллекция"
        ordering = ["name"]

    def __str__(self):
        return self.name
