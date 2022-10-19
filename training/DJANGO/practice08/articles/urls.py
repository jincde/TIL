from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("write/", views.write, name="write"),
    path("detail/<int:pk>", views.detail, name="detail"),
]
