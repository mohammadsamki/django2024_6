from django.shortcuts import HttpResponse, render

from .models import Users

# Create your views here.


def home(request):
    print('test home')
    name = "ahmad"
    # get all the data in this modale
    users = Users.objects.all()
    print(users)

    context = {
        'name':name,
        "worked":True,
        "users":users

    }

    return  render(request, 'home.html', context=context)

