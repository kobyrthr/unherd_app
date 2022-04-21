from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
	path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.Index.as_view(), name="home"),
    path('new/',views.Event_Create.as_view(),name='event_create'),
    path('events/<int:pk>', views.EventDetail.as_view(),name="event_detail")
]