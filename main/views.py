# Create your views here.
# main/views.py
from django.shortcuts import render
from .models import Member, Event, Petition

def home(request):
    return render(request, 'main/home.html')

def members(request):
    members = Member.objects.all()
    return render(request, 'main/members.html', {'members': members})

def events(request):
    events = Event.objects.all()
    return render(request, 'main/events.html', {'events': events})

def petitions(request):
    petitions = Petition.objects.all()
    return render(request, 'main/petitions.html', {'petitions': petitions})
