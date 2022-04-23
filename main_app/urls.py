from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# this like app.use() in express
urlpatterns = [
	path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.Index.as_view(), name="home"),
    path('new/',views.Event_Create.as_view(),name='event_create'),
    path('<int:pk>/', views.EventDetail.as_view(),name="event_detail")
]