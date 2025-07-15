from django.urls import path
from .views import *

app_name = "singer"

urlpatterns = [
    path('', singer_list_create),
    path('<int:singer_id>', singer_detail_update_delete),
    path('<int:singer_id>/song', song_read_create),
    path('tags/<str:tags_name>', find_tag),
]
