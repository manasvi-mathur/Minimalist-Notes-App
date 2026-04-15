from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/notes/', views.api_notes, name='api_notes'),
    path('api/add/', views.add_note, name='add_note'),
    path('api/delete/<int:note_id>/', views.delete_note, name='delete_note'),
    path('api/update/<int:note_id>/', views.update_note, name='update_note'),
]
