from django.urls import path
from .views import home,  HomeView

urlpatterns = [
    # This is the new path you need to add. It maps the root URL ('') to your HomeView.
    path('', HomeView.as_view(), name='class_home_page'),

    # Maps the 'home' function-based view to the 'home/' URL
    path('home/', home, name='home'),


]
