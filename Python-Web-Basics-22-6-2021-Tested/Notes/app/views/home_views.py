from django.shortcuts import render

from app.forms import ProfileForm
from app.models import Profile, Note


def home_page(request):
    profile = Profile.objects.first()
    notes = Note.objects.all()
    if profile:
        context = {
            'profile': profile,
            'notes': notes,
        }
        return render(request, 'home-with-profile.html', context)

    context = {
        'form': ProfileForm,
    }
    return render(request, 'home-no-profile.html', context)
