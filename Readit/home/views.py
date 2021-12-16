from django.http.request import RAISE_ERROR
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . models import User ,Question, Answer,Category
import datetime
import pytz

# Create your views here.
def start_up(request):
    if request.method == 'POST':
        try:
            recieved_data = request.POST
            id_no = recieved_data['id']
            select = recieved_data['select']
            user = User.objects.get(id = id_no)
            questions = Question.objects.order_by('-time').exclude(author = user)
            if select == 'select_0#22':
                return render(request,'home/home.html',{
                    'id' : id_no,
                    'user' : user,
                    'categories' : Category.objects.all(),
                    'questions' : questions,
                    'user_count' : User.objects.all().count(),
                    'total_questions' : Question.objects.all().count(),
                })
            if select == 'select_0#21':
                photo_added = request.FILES['file_']
                user = User.objects.get(id = int(id_no))
                user.profile_image = photo_added
                user.save()
                return render(request,'home/home.html',{
                    'id' : id_no,
                    'user' : user,
                    'categories' : Category.objects.all(),
                    'questions' : questions,
                    'user_count' : User.objects.all().count(),
                    'total_questions' : Question.objects.all().count(),
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
                    questions = Question.objects.order_by('-time').exclude(author=user)
                    return render(request,'home/home.html',{
                        'id' : user.id,
                        'user' : user,
                        'categories' : Category.objects.all(),
                        'questions' : questions,
                        'user_count' : User.objects.all().count(),
                        'total_questions' : Question.objects.all().count(),
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

def search_results(request):
    if request.method == 'POST':
        received_info = request.POST
        id_no = received_info['id']
        user_id = received_info['user_id']
        if received_info['select'] == 'select#@search@input':
            results = User.objects.filter(name__contains = received_info['search']).exclude(id=id_no)
            return render(request,'home/search_results.html',{
                'id' : id_no,
                'users' : results
            })
        elif received_info['select'] == 'select#@search@result': 
            user = User.objects.get(id = user_id)
            if user_id == id_no:
                return render(request,'home/my_profile.html',{
                    'id' : id_no,
                    'user' : user
                })
            return render(request,'home/user_profile.html',{
                'id' : id_no,
                'user' : user
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
        elif input_object['select'] == 'select#@home@page' :
            questions = Question.objects.order_by('-time').exclude(author=user)
            return render(request,'home/home.html',{
                'id' : id_no,
                'user' : user,
                'categories' : Category.objects.all(),
                'questions' : questions,
                'user_count' : User.objects.all().count(),
                'total_questions' : Question.objects.all().count(),
            })

def post_question(request):
    if request.method == 'POST':
        solutions = request.POST
        id_no = solutions['id']
        user = User.objects.get(id=id_no)
        question_text = solutions['comments']
        selected_category = Category.objects.get(category = solutions['category'])
        IST = pytz.timezone('Asia/Kolkata')
        Question.objects.create(question = question_text,
            time = datetime.datetime.now(IST).time(),
            date = datetime.datetime.now(IST).date(),
            category = selected_category,
            author = user)
        questions = Question.objects.order_by('-time')#.exclude(author=user)
        return render(request,'home/home.html',{
            'id' : id_no,
            'user' : user,
            'categories' : Category.objects.all(),
            'questions' : questions,
            'user_count' : User.objects.all().count(),
            'total_questions' : Question.objects.all().count(),
        })

def category_filter(request):
    if request.method == 'POST':
        selected_category = request.POST['category']
        selected_filter = request.POST['filter']
        id_no = request.POST['id']
        user = User.objects.get(id=id_no)
        questions = Question.objects.order_by('-time')
        if selected_category != 'Categories':
            category_got = Category.objects.get(category=selected_category)
            questions = questions.filter(category=category_got)
        if selected_filter != 'Filter by':
            if selected_filter == 'Oldest':
                questions = questions.order_by('time')
            # elif selected_filter == 'Replys':
            #     questions = questions.order_by('questions.answers.count()')
        return render(request,'home/home.html',{
            'id' : id_no,
            'user' : user,
            'categories' : Category.objects.all(),
            'questions' : questions,
            'user_count' : User.objects.all().count(),
            'total_questions' : Question.objects.all().count(),
        })



