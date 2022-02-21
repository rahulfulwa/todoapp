from django.urls import path
from todo import views

urlpatterns = [
    path('', views.index, name="todo"),
    path('<int:item_id>/del/', views.remove, name="delete"),
]
