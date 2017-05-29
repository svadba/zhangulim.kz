from django.views import generic
from .models import Article


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    model = Article
    # paginate_by = 1

    def get_queryset(self):
        articles = Article.objects.all()
        return articles


class DetailView(generic.DetailView):
    model = Article
    context_object_name = 'article1'
    template_name = 'blog/detail.html'

