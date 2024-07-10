from app1.models import Category,Item,Favo
from django.shortcuts import render,redirect
def dropdown(request):
    category = Category.objects.all()
    return {'links':category}


