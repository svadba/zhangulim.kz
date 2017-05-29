from django.contrib import admin
from .models import *
from .widgets import *
from django import forms
from django.shortcuts import redirect


# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PhotoAdminForm(forms.ModelForm):

    class Meta:
        model = Photo
        widgets = {'image': MultiFileInput}
        exclude = [""]



class PhotoAdmin(admin.ModelAdmin):
    form = PhotoAdminForm


class PhotoAdmin(admin.ModelAdmin):
    form = PhotoAdminForm
    list_display = ['image_img', 'image']

    def add_view(self, request, *args, **kwargs):
        images = request.FILES.getlist('image',[])
        is_valid = PhotoAdminForm(request.POST, request.FILES).is_valid()

        if request.method == 'GET' or len(images)<=1 or not is_valid:
            return super(PhotoAdmin, self).add_view(request, *args, **kwargs)
        for image in images:
            album_id=request.POST['album']
            photo = Photo(album_id=album_id, image=image)
            photo.save()
        return redirect('/admin/albome/photo/')


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)