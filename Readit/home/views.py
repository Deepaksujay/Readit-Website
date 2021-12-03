from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . models import User ,Question, Answer

# Create your views here.
def start_up(request):
    return render(request,'home/index.html',{
                'error' : False,
                'already_registered' : False,
                'wrong_credentials' : False,
                'password_match' : False,
                'not_registered' : False
            })

def load_up_sign_in(request):
    if request.method == 'POST':
        main_object = request.POST
        user_email = main_object['email']
        user_password = main_object['pswd']
        try:
            user = User.objects.get(email = user_email)
            if user.password == user_password:
                return HttpResponse("Success")
            else:
                return render(request,'home/index.html',{
                            'error' : True,
                            'already_registered' : False,
                            'wrong_credentials' : True,
                            'password_match' : False,
                            'not_registered' : False
                       })
        except:
            return render(request,'home/index.html',{
                        'error' : True,
                        'already_registered' : False,
                        'wrong_credentials' : False,
                        'password_match' : False,
                        'not_registered' : True
                    })


def load_up_sign_up(request):
    if request.method == 'POST':
        main_object = request.POST
        try:
            if main_object['pswd'] == main_object['cnfrmpswd']:
                User.objects.create(name=main_object['txt'],email=main_object['email'], password=main_object['pswd'])
            else:
                return render(request,'home/index.html',{
                            'error' : True,
                            'already_registered' : False,
                            'wrong_credentials' : False,
                            'password_match' : True,
                            'not_registered' : False
                        })
            return render(request,"home/index_profile.html")
        except:
            return render(request,'home/index.html',{
                    'error' : True,
                    'already_registered' : True,
                    'wrong_credentials' : False,
                    'password_match' : False,
                    'not_registered' : False
                    })

def home(request):
    pass

def image(request):
    return render(request,"home/index_profile.html")