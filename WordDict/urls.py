from django.conf.urls import url
from . import views

app_name = 'WordDict'

urlpatterns = [
    url('dict/',views.oxford, name='dict'),
]
