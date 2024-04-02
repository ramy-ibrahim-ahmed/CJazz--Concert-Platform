from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.forms import ValidationError
from django.contrib import messages
from django.core.validators import MinValueValidator

# Create your views here.
def index(request):

    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'about':About.objects.get(id=1),
        'artists':Artist.objects.all(),
        'parties':Party.objects.all(),
        'plans':Plan.objects.all(),
        'form':form,
        'submitted':submitted,
    }
    return render(request, 'pages/home.html',context)

#-----------------------------------------------------------------------

def ticket(request):
    submitted = False
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = TicketForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form':form,
        'submitted':submitted,
    }
    return render(request, 'pages/ticket.html', context)
