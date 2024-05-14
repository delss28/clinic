from django.shortcuts import render



def profile(request):
    context = {

    }
    return render(request,'users/profile.html',context)

def logout(request):
    ...