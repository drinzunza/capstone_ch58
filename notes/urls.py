from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.NoteList.as_view(), name="note_list"),
    path("detail/<int:pk>/", views.NoteDetail.as_view(), name="note_detail"),
]
