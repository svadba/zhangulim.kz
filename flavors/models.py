from django.db import models
from django.utils import timezone

class Flavor(models.Model):
    image = models.ImageField('изображение', upload_to="flavors/photos")
    title = models.CharField("название", max_length=50)
    price = models.IntegerField("цена")
    description = models.TextField("описание")
    pub_date = models.DateTimeField(auto_now_add=timezone.now())

    class Meta:
        verbose_name = "Букет"
        verbose_name_plural = "Букеты"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/flavor/" + str(self.id)
