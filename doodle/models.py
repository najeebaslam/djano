from django.db import models

class Mdate(models.Model):
    mdate = models.DateTimeField('meeting date', auto_now_add=True)

class Room(models.Model):
    location = models.CharField(max_length=200)
    capasity = models.IntegerField(default=10)
    
class Meeting (models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    r_votes = models.IntegerField(default=5)
    mdate = models.ForeignKey(Mdate, blank=True, null=True)
    room = models.ForeignKey(Room, blank=True, null=True)

class Choice(models.Model):
    meeting = models.ForeignKey(Meeting)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    choice_date = models.DateTimeField()