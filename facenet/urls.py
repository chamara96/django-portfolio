from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('train_face/', views.train_face, name="train_face"),
]
