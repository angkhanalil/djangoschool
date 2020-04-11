from django.urls import path
from .views import HomePage #call homepage function
urlpatterns ={
    # localhost:8000
    path('',HomePage)
}