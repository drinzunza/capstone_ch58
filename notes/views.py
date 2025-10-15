from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Note

"""
Class-based views:

View         = Generic View
ListView     = get a list of records
DetailView   = get a single (detail) record
CreateView   = create a new record
DeleteView   = remove a record
UpdateView   = modify an existing record
LoginView    = LogIn

"""

# Create your views here.
class NoteList(ListView):
    model = Note
    template_name = "notes/list.html"


class NoteDetail(DetailView):
    model = Note
    template_name = "notes/details.html"