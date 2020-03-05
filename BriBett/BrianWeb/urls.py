from django.conf.urls import url
from . import views

app_name = 'BrianWeb'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^portfolio', views.portfolio, name='portfolio'),
    url(r'^contact', views.contact, name='contact')
]