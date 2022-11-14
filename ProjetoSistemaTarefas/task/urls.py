from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('tasks/', views.index, name="list"),
    path('update/<int:pk>', views.updateTask, name="update"),
    path('delete/<int:pk>', views.deleteTask, name="delete"),
]