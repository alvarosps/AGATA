from django.conf.urls import url
from textMining import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^select_text', views.select_text, name = 'select_text'),
        url(r'^edit_text', views.edit_text, name = 'edit_text'),
        url(r'^generate_aiml', views.generate_aiml, name = 'generate_aiml'),
]