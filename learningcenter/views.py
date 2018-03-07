from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View
from .models import Article
# Create your views here.
class ListView(View):
    def get(self, request):
        article_list=Article.objects.all().order_by('-created')
        return render(request,'learningcenter_index.html',
                      {'article_list':article_list}
                      )

class DetailView(View):
    def get(self, request,article_id):
        try:
            article =Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, 'learningcenter_detail.html', {'article': article})
