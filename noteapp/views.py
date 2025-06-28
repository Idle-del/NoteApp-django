from django.shortcuts import render

from note.models import Note

def home(request):
    notes = Note.objects.all()
    context = {
        'notes': notes
    }
    return render(request, 'home.html', context)