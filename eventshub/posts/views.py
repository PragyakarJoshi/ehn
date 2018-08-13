from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Event, Category
from .forms import EventForm

def home(request):
    category_list = Category.objects.all()
    event_list = Event.objects.all()
    context = {
        "categories" : category_list,
        "events" : event_list,
        "title": "Events List",
    }
    return render(request, "eventlist.html", context)

def event_add(request):
    form = EventForm(request.POST or None) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Sucessfully Added New Event!")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Error! Could not Add New Event.")
    context = {
        "title": "Add New Event",
        "form": form 
    }
    return render(request, "eventadd.html", context)

def event_update(request, id=None):
    instance = get_object_or_404(Event, id=id)
    form = EventForm(request.POST or None, instance = instance) 
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Sucessfully Updated Event Details!")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Error! Could not Update Event Details.")
    context = {
        "title": "Update Event",
        "instance": instance,
        "form": form
    }
    return render(request, "eventupdate.html", context)

def event_delete(request, id=None):
    instance = get_object_or_404(Event, id=id)
    instance.delete()
    messages.success(request, "Sucessfully Deleted Event")
    return redirect("events:list")

def event_details(request, id):
    instance = get_object_or_404(Event, id=id)
    context = {
        "title": "Event Details",
        "instance": instance,
    }
    return render(request, "eventdetails.html", context)


