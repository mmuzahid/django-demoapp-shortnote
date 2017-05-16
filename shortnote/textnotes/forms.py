from django import forms
from shortnote.textnotes.models import TextNote


class CreateTextNote(forms.ModelForm):
    class Meta:
        model = TextNote
        fields = ['owner', 'subject', 'content', 'remind_at']
