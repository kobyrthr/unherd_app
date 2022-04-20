from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Index.as_view(), name="home"),
    path('events/<int:pk>', views.EventDetail.as_view(),name="event_detail")
]