from django.shortcuts import render
from django.views import View
from .models import blogMolde

# Create your views here.

class blogView(View):
    def get(self, request):

        return render(request, '')
