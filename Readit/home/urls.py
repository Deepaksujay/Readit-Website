from django.urls import path
from . import views

urlpatterns = [
    path('',views.start_up, name = 'start-up'),
    path('/load-up-sign-in',views.load_up_sign_in, name = 'load-up-sign-in'),
    path('/load-up-sign-up',views.load_up_sign_up, name = 'load-up-sign-up'),
    path('home',views.home,name = 'home'),
    path('contact-us',views.contact_us,name='contact-us'),
    path('about-us',views.about_us,name='about-us'),
    path('my-profile',views.my_profile,name='my-profile'),
    path('search-results',views.search_results,name='search-results')
]
