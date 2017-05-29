from django.views import generic
from .models import Photo, Album


class IndexView(generic.ListView):
    template_name = 'albome/index.html'
    context_object_name = 'albums'
    model = Photo
    # paginate_by = 1

    def get_queryset(self):
        albums = Album.objects.all()
        return albums


class DetailView(generic.ListView):
    template_name = 'albome/detail.html'
    context_object_name = 'photos'
    model = Photo

    def get_queryset(self):
        photos = Photo.objects.all()
        album_filter = Album.objects.get(slug=self.kwargs['album'])
        photos = photos.filter(album=album_filter)
        return photos
