from django.shortcuts import render, redirect
from app.forms import NotesForm, NotesFormDisabled
from app.models import Note


def create_or_edit(request, note, template):
    if request.method == 'GET':
        context = {
            'form': NotesForm(instance=note),
            'note': note
        }
        return render(request, template, context)
    else:
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'form': NotesForm(instance=note),
            'note': note
        }
        return render(request, template, context)


def create_note(request):
    return create_or_edit(request, Note(), 'note-create.html')


def edit_note(request, pk):
    return create_or_edit(request, Note.objects.get(pk=pk), 'note-edit.html')


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': NotesFormDisabled(instance=note),
            'note': note
        }
        return render(request, 'note-delete.html', context)
    else:
        note.delete()
        return redirect('home page')


def details_note(request, pk):
    note = Note.objects.get(pk=pk)
    context = {
        'note': note
    }
    return render(request, 'note-details.html', context)
