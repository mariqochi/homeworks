from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    This view returns a simple HTTP response to confirm that the URL is working.
    """
    return HttpResponse("<h1>Hello, this is the blog app home page!</h1>")
