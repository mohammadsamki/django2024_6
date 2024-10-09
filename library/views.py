from django.shortcuts import HttpResponse, render

# Create your views here.


def home(request):
    print('test home')
    name= "ahmad"
    context={
        'name':name,
        "worked":True

    }

    return  render(request, 'home.html',context=context)

