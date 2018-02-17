from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.memory_list, name='memory_list'),
]