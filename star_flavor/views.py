from django.views import generic
from .models import StarFlavor


class IndexView(generic.ListView):
    template_name = 'star_flavor/star_flavors.html'
    context_object_name = 'list'
    model = StarFlavor
    # paginate_by = 1

    def get_queryset(self):
        star = StarFlavor.objects.all()
        return star


class DetailView(generic.DetailView):
    model = StarFlavor
    context_object_name = 'flavor'
    template_name = 'star_flavor/detail.html'
