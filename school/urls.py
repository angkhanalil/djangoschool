from django.urls import path
from .views import HomePage,base #call homepage function
# from .views import base
urlpatterns ={
    # localhost:8000
    path('',HomePage),
    path('base/',base)
}