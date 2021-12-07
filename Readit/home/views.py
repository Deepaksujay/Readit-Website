from django.http.request import RAISE_ERROR
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . models import User ,Question, Answer

user = None
# Create your views here.
def start_up(request):
    if request.method == 'POST':
        try:
            recieved_data = request.POST
            id_no = recieved_data['id']
            select = recieved_data['select']
            user = User.objects.get(id = id_no)
            if select == 'select_0#22':
                return render(request,'home/home.html',{
                    'id' : id_no,
                    'user' : user
                })
            if select == 'select_0#21':
                photo_added = request.FILES['file_']
                user = User.objects.get(id = int(id_no))
                user.profile_image = photo_added
                user.save()
                return render(request,'home/home.html',{
                    'id' : id_no,
                    'user' : user
                })
        except:
            return HttpResponse("Something is wrong")

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
                if user.profile_image:
                    return render(request,'home/home.html',{
                        'id' : user.id,
                        'user' : user
                    })
                else: 
                    return render(request,"home/index_profile.html",{
                        "id" : user.id,
                        'user' : user
                    })
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
                email = main_object['email']
                email = email.lower()
                user = User.objects.create(name=main_object['txt'],email=email, password=main_object['pswd'])
            else:
                return render(request,'home/index.html',{
                            'error' : True,
                            'already_registered' : False,
                            'wrong_credentials' : False,
                            'password_match' : True,
                            'not_registered' : False
                        })
            return render(request,"home/index_profile.html",{
                'id' : user.id,
                'user' : user
            })
        except:
            return render(request,'home/index.html',{
                    'error' : True,
                    'already_registered' : True,
                    'wrong_credentials' : False,
                    'password_match' : False,
                    'not_registered' : False
                    })

def contact_us(request):
    if request.method == 'POST':
        id_no = request.POST['id']
        user = User.objects.get(id = int(id_no))
        return render(request,'home/contact_us.html',{
            'user' : user,
            'id' : id_no,
            'submitted' : False
        })

def about_us(request):
    if request.method == 'POST':
        id_no = request.POST['id']
        return render(request,'home/about_us.html',{
            'id' : id_no
        })

def my_profile(request):
    if request.method == 'POST':
        id_no = request.POST['id']
        user = User.objects.get(id = int(id_no))
        return render(request,'home/my_profile.html',{
            'id' : id_no,
            'user' : user
        })

def home(request):
    if request.method == 'POST':
        input_object = request.POST
        id_no = input_object['id']
        user = User.objects.get(id = int(id_no))
        if input_object['select'] == 'select#@contact@us':
            return render(request,'home/contact_us.html',{
                'user' : user,
                'id' : id_no,
                'submitted' : True
            })
        if input_object['select'] == 'select#@home@page' :
            return render(request,'home/home.html',{
                'id' : id_no,
                'user' : user
            })
    

