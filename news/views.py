from django.shortcuts import render
from news.models import Article
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from news.forms import ArticleForm

# Create your views here.
class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main Page'
        return context

def text(request, pk):
    articles = Article.objects.get(id=pk)
    return render(request, 'text.html', {'article': articles, 'title': articles.name})


class AddArticle(CreateView):
    form_class = ArticleForm
    model = Article
    template_name = 'create_article.html'
    success_url = reverse_lazy('index')
