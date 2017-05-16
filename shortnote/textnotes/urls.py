from django.conf.urls import url
from shortnote.textnotes import views

urlpatterns = [
    url(r'^new', views.new_textnote),
    url(r'^get', views.get_textnote),
    url(r'^post', views.post_textnote),
    url(r'^api/get/(\d+)', views.get_json_textnote_by_id),
]
