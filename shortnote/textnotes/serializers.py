from rest_framework import serializers
from shortnote.textnotes.models import TextNote


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextNote
        fields = ['owner', 'subject', 'content', 'remind_at']
