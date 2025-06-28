from django.shortcuts import redirect, render

from .models import Note

# Create your views here.
def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']

        Note.objects.create(title=title, text=text)
    
        return redirect('home')
    return render(request, 'addnotes.html')