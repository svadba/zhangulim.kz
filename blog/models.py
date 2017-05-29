from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField('название', max_length=200)
    description = models.CharField('Краткое описание', max_length=500)
    text = models.TextField('описаний')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    images = models.ImageField("фотография", upload_to="blog/photos", default="", blank=True)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title"]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
