from django.urls import path
# from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    path('', views.index, name='index'),
    path('', views.results, name='results'),
    path('', views.vote, name='vote'),

]
