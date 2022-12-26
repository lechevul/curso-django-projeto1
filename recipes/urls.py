
from django.urls import path

from recipes.views import contato, home, sobre

# HTTP request


urlpatterns = [
    path('sobre/', sobre),
    path('contato/', contato),
    path('', home),
]
