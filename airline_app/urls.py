from django.urls import path
from . import views

urlpatterns = [
    path('', views.airplane_list, name='airplane_list'),
    path('new', views.airplane_new, name='airplane_new'),
    path('edit/<int:pk>', views.airplane_edit, name='airplane_edit'),
    path('delete/<int:pk>', views.airplane_delete, name='airplane_delete'),
]