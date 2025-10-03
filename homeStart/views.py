import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from homeStart.forms import LogMessageForm
from homeStart.models import LogMessage
from django.views.generic import ListView


def home(request):
    return render(request, "homeStart/home.html")

def homeStart_there(request, name):
    print(request.build_absolute_uri())
    return render(
        request,
        'homeStart/homeStart_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def about(request):
    return render(request, "homeStart/about.html")

def contact(request):
    return render(request, "homeStart/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "homeStart/log_message.html", {"form": form})
    
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context