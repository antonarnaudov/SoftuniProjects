from django import forms

from app.models import Profile, Note


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class NotesFormDisabled(NotesForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True
