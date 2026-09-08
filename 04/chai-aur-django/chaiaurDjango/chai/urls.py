
from django.urls import path
from . import views

#localhost:8000/chai -> its in the main urls.py file
#localhost:8000/chai/order -> its written here

urlpatterns = [
    
    path('', views.all_chai, name="all_chai"),
    # path('about/', views.about, name = "order"),

]
