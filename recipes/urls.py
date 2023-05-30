from django.urls import path


# from recipes import views
# (o . indica que o arquivo que está sendo buscado é irmão deste arquivo, ou seja, da pasta que estamos importe views)
from . import views

# recipes:recipe
app_name = 'recipes'

# dominio/recipes/...
urlpatterns = [
    path('', views.home, name="home"),  # HOME
    path('recipes/<int:id>/', views.recipes, name="recipe"),

]
