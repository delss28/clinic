from django.shortcuts import render

# Create your views here.
def services(reguest):
    return render(reguest,'services/services.html')

def service(reguest):
    return render(reguest,'services/service.html')