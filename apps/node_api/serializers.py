from rest_framework import serializers
from .models import NoteModel, SubscribeToNewsletter


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteModel
        fields = '__all__'
        
class SubscribeSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = SubscribeToNewsletter
        fields = ('email',)        
