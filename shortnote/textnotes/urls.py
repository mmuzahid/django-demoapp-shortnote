from django.conf.urls import url
from shortnote.textnotes import views

urlpatterns = [
    url(r'^new', views.new_textnote),
    url(r'^get', views.get_textnote),
    url(r'^post', views.post_textnote),
    url(r'^api/get/by/id/(\d+)', views.get_json_textnote_by_id),
    url(r'^api/get/by/user/(\d+)', views.get_json_textnote_by_user),
    url(r'^api/post/new', views.post_json_textnote),
]
