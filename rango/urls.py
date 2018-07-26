from django.conf.urls import url
from rango import views

urlpatterns = [
    # Maps the index view to the http://127.0.0.1:8000/rango/ address.
    url(r'^$', views.index, name='index'),
    # Maps the index view to the http://127.0.0.1:8000/rango/about address.
    url(r'^about/', views.about, name='about'),
]