from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "title", 
            "description",
            "location",
            "date",
            "category",
            "price",
            "registration",
            "opening_time",
            "closing_time"
        ]
