from django import forms
from .models import Meeting, Choice, Mdate, Room

#form used for creating new meeting
class MeetingForm(forms.Form):
    title = forms.CharField(label="Title of Meeting")
    r_votes = forms.IntegerField(label="Required Votes to set time")

#form used for assigning room to meeting
class RoomForm(forms.Form):
	room = forms.ModelChoiceField(queryset = Room.objects.all() )
