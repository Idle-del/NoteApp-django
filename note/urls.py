
from django.urls import path

from . import views

urlpatterns = [
    # Path to add a new note
    path('add_note/', views.add_note, name='add_note'),
    # Path to edit existing notes
    path('edit_note/<int:pk>/', views.edit_note, name = 'edit_note'),
    # Path to delete a note
    path('delete_note/<int:pk>/', views.delete_note, name = 'delete_note')
]
