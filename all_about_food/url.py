from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('search',views.searchView,name='search'),
    path('', views.homePageView,name='homepage'),
    path('restaurent/<int:id>',views.restaurentView,name='restaurent'),
    path('<str:category>',views.categoryView,name='category'),

]