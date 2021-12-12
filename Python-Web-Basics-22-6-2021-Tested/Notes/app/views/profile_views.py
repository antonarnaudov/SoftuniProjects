from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from app.forms import ProfileForm
from app.models import Profile, Note


def profile_view(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    notes.count = Note.objects.count()

    context = {
        'profile': profile,
        'notes': notes
    }

    return render(request, 'profile.html', context)


@require_POST
def profile_create(request):
    form = ProfileForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home page')


def profile_delete(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()

    profile.delete()
    notes.delete()
    return redirect('home page')
