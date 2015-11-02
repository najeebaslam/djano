
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from doodle.forms import *
from django.shortcuts import * 

from .models import Meeting, Choice, Mdate, Room

#index method displas all list of created meetings 
def index(request):
    latest_meeting_list = Meeting.objects.order_by('-pub_date')[:5]
    context = {'latest_meeting_list': latest_meeting_list}
    return render(request, 'doodle/index.html', context)

# display meeting details, if date is not selected it will lead you to vote for date
# if date is decided it will leads you to chose room 
# if room is selected it will leads you to result, will all details of meeting with time and room no
def detail(request, meeting_id):
    meeting =  get_object_or_404(Meeting, pk=meeting_id)
    mdate = Mdate.objects.filter(meeting = meeting)
    room = Room.objects.filter(meeting = meeting)
    if (room.exists()):
        return HttpResponseRedirect(reverse('doodle:results', args=(meeting.id,)))
    elif ( mdate.exists()): 
        return HttpResponseRedirect(reverse('doodle:room', args=(meeting.id,)))
    else:
        return render(request, 'doodle/detail.html', {'meeting': meeting})

#this method handles assigning room to the meeting after chosing date for meeting
def room(request, meeting_id):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if(form.is_valid()):
            room = get_object_or_404(Room, pk=request.POST['room'])
            meeting = get_object_or_404(Meeting, pk=meeting_id)
            room.meeting_set.add(meeting)
            room.save()
            meeting.room = room
            meeting.save()
            message = "Congrats!! Room has been assigned"
            return HttpResponseRedirect(reverse('doodle:results', args=(meeting.id,)))
        else:
            message = "Room is not assigned"
        return render_to_response('doodle/room.html',
                {'success': message},
                context_instance=RequestContext(request))
    else:
        return render_to_response('doodle/room.html',
                {'form':RoomForm()},
                context_instance=RequestContext(request, { 'meeting_id': meeting_id}))

# this method is used to create new meetings
def new_meeting(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        
        if(form.is_valid()):
            # import pdb; pdb.set_trace()
            new_meeting = Meeting(title =  request.POST['title'], r_votes= request.POST['r_votes'], pub_date= timezone.now())
            new_meeting.save()
            message = "Congrats!! New Meeting has been created."
        else:
            message = "sorry something went wrong"
        return render_to_response('doodle/new.html',
                {'success': message},
                context_instance=RequestContext(request))
    else:
        return render_to_response('doodle/new.html',
                {'form':MeetingForm()},
                context_instance=RequestContext(request))

#this method is used to vote for any choice 
def vote(request, meeting_id):
    p = get_object_or_404(Meeting, pk=meeting_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'doodle/detail.html', {
            'meeting': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        if selected_choice.votes >= selected_choice.meeting.r_votes :
        	mdate = Mdate(mdate= selected_choice.choice_date)
        	mdate.save()
        	mdate.meeting_set.add(selected_choice.meeting)
        	mdate.save()
        	selected_choice.meeting.mdate = mdate
        	selected_choice.meeting.save()
        return HttpResponseRedirect(reverse('doodle:results', args=(p.id,)))

#this method shows all status of meeting at any stage 
def results(request, meeting_id):
    meeting = get_object_or_404(Meeting, pk=meeting_id)
    mdate = Mdate.objects.filter(meeting = meeting)
    room = Room.objects.filter(meeting = meeting)
    can_vote = mdate.exists()
    has_room = room.exists()
    if can_vote :
        mdate=mdate[0]
    if has_room :
        room = room[0]
    return render(request, 'doodle/result.html', {'meeting': meeting, 'mdate': mdate, 'room': room, 'can_vote': can_vote, 'has_room': has_room})