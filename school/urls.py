from django.urls import path
from .views import HomePage,AboutPage,ContactUs #call homepage function
# from .views import base
urlpatterns ={
    # localhost:8000
    path('',HomePage,name='home-page'),
    path('about/',AboutPage ,name='about-page'),
    path('contact/',ContactUs ,name='contact-page')
}