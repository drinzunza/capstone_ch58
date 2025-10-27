from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, View
from .models import Note, Comment
from .forms import CreateCommentForm


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


class CreateComment(View):
    def post(self, request):
        id = request.POST.get("id")
        content = request.POST.get("content")

        # get the Note object 
        note = Note.objects.get(pk=id)

        # create the comment
        Comment.objects.create(
            note = note,
            content = content,
            author = request.user
        )

        # send back to details page
        return redirect("note_detail", pk=id)