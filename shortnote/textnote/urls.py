from django.conf.urls import url
from shortnote.textnote import views

urlpatterns = [
    url(r'^new', views.new_textnote),
    url(r'^get', views.get_textnote),
    url(r'^post', views.post_textnote),
]
