
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse # You need to import HttpResponse
from django.views import View


def home(request):
    return HttpResponse("Hello, This is Home Page")
#def not_found(request):
    return HttpResponse("Not Found 404") #
# Create your views here.
class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page!")