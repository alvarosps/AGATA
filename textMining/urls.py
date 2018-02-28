from django.conf.urls import url
from textMining import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^selecttext', views.select_text, name = 'selecttext'),
        url(r'^edittext', views.edit_text, name = 'edittext'),
        url(r'^generateaiml', views.generate_aiml, name = 'generateaiml'),
]