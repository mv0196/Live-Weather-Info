from django.conf.urls import url
from . import views

app_name = 'Weather'

urlpatterns = [
    url('index',views.index, name='index'),
    url('delete/(?P<id>\d+)/', views.delete_city, name='delete_city'),
    url('feedback/', views.form, name='feed'),
]
