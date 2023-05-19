from django.urls import path

from recipes.views import home, contato, sobre

# dominio/recipes/...
urlpatterns = [
    path('', home),  # HOME
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato)  # /contato/
]
