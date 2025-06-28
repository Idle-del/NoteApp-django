from django.shortcuts import get_object_or_404, redirect, render

from .models import Note

# Create your views here.
def add_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']

        Note.objects.create(title=title, text=text)
    
        return redirect('home')
    return render(request, 'addnotes.html')

def edit_note(request, pk):
    get_note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        new_title = request.POST['title']
        new_text = request.POST['text']
        get_note.title = new_title
        get_note.text = new_text
        get_note.save()
        return redirect('home')
    else:
        context = {
            'get_note' : get_note
        } 
        return render(request, 'editnote.html', context)
    # return HttpResponse('Edit Note Page')

def delete_note(request, pk):
    Note.objects.filter(pk=pk).delete()
    return redirect('home')