from django.db import models
# Create your models here.


class Album(models.Model):
    title = models.CharField('название', max_length=100, blank=True, default='')
    image = models.ImageField('изображение', upload_to="albome/photos")
    date = models.DateTimeField()
    slug = models.SlugField(max_length=150, db_index=True, unique=True)

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"
        ordering = ['title']

    def __str__(self):
        return self.title


class Photo(models.Model):
    album = models.ForeignKey(Album, verbose_name='альбом', related_name='photos')
    image = models.ImageField('изображение', upload_to="albome/photos")
    title = models.CharField('название', max_length=255, blank=True, default='')

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фотографии"
        ordering = ['title']

    def image_img(self):
        if self.image:
            return '<img src="%s" width="100"/>' % self.image.url
        else:
            return '(none)'

    image_img.short_description = 'Thumb'
    image_img.allow_tags = True
