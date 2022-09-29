from django.urls import path
from . import views

app_name = 'Todo'

urlpatterns = [
  path('', views.index, name='index'),
  path('create/', views.create, name='create'),
  path('change/<int:Todo_pk>', views.change, name='change'),
  path('delete/<int:Todo_pk>', views.delete, name='delete'),
  # path('modify/<int:Todo_pk>', views.modify, name='modify'),
  path('update/<int:Todo_pk>', views.update, name='update'),
]