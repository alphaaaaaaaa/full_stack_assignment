from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Restaurent,Dish
# Create your views here.
def homePageView(request):
    restaurents = Restaurent.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(restaurents, 3)
    try:
        restaurents = paginator.page(page)
    except PageNotAnInteger:
        restaurents = paginator.page(1)
    except EmptyPage:
        restaurents = paginator.page(paginator.num_pages)
    context = {
        'restaurents':restaurents,
        'active':'home',
    }
    return render(request,'homepage.html',context)
def categoryView(request,category):
    category = category.replace('-', ' ')
    image = category + ".jpg"
    restaurents = Restaurent.objects.filter(category=category)
    page = request.GET.get('page', 1)
    paginator = Paginator(restaurents, 3)
    try:
        restaurents = paginator.page(page)
    except PageNotAnInteger:
        restaurents = paginator.page(1)
    except EmptyPage:
        restaurents = paginator.page(paginator.num_pages)
    context = {
        'restaurents':restaurents,
        'image':image,
        'category':category,
        'active':category,
    }
    return render(request,'categories.html',context)
def restaurentView(request,id):
    restaurent = Restaurent.objects.get(id=id)
    print("test",restaurent.image)
    context = {
        'restaurent':restaurent
    }
    return render(request,'restaurent.html',context)

def searchView(request):
    q = request.GET.get("q")
    restaurents = Restaurent.objects.filter(address__icontains=q)
    
    dishes = Dish.objects.filter(name__icontains=q,description__icontains=q)
    
    context = {
        'restaurents':restaurents,
        'dishes':dishes,
        'search':True
    }
    return render(request,'homepage.html',context)