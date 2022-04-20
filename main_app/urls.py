from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Index.as_view(), name="home")

]