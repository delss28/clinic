from django.shortcuts import render

from main.models import Service

# Create your views here.
def services(reguest):
    return render(reguest,'services/services.html')

def service(reguest, service_slug):

    service = Service.objects.get(slug=service_slug)

    context = {
        'service': service
    }

    return render(reguest,'services/service.html', context)
