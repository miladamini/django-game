from django.shortcuts import render
from django.views import View
from .models import lDitaile, gameMode
from blog.models import blogMolde


# Create your views here.


class HomeView(View):
    def get(self, request):
        game = lDitaile.objects.all().reverse()[:6]
        like = lDitaile.objects.order_by('like').all().reverse()[:5]
        gameModeFilteer = gameMode.objects.all()
        blogquery = blogMolde.objects.all().reverse()[:4]
        return render(request, 'index.html',
                      {'game': game, 'like': like, 'gameModeFilteer': gameModeFilteer, 'blogquery': blogquery})
