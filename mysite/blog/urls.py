from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
  path("", views.index, name="index"),
  path("<int:post_id>/", views.detail, name="detail"),
  path("reply/create/<int:post_id>/", views.reply_create, name="reply_create"),
  path("post/create/", views.post_create, name="post_create"),
]