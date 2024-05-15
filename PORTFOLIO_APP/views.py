from datetime import datetime, timezone
from django.shortcuts import render,HttpResponse
import pytz
from .models import *

# Create your views here.

def portfolio(request):
    utc_time = datetime.now(timezone.utc)
    india_time = utc_time.astimezone(pytz.timezone('Asia/Kolkata'))
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact_query = Contact.objects.create(name = name, email = email, subject = subject, message = message,date_time = india_time)
        contact_query.save()
        return HttpResponse('<script>alert("Sent successfully"); window.location.href = "/";</script>')
    return render(request, 'portfolio.html')
