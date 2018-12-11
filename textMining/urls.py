from django.conf.urls import url
from textMining import views
from django.urls import include, path

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^aiml', views.aiml, name='aiml'),
    url(r'^upload-aiml', views.upload_aiml, name='upload_aiml'),
    url(r'^selecttext', views.select_text, name = 'selecttext'),
    url(r'^edittext', views.edit_text, name = 'edittext'),
    url(r'^edit-text-upado', views.edit_text_upado, name = 'edit_text_upado'),
    url(r'^generateaiml', views.generate_aiml, name = 'generateaiml'),
    url(r'^change-aiml', views.change_aiml, name = 'change-aiml'),
    url('^sobre', views.about, name='sobre'),
    url('^tutorial', views.tutorial, name='tutorial'),
]
