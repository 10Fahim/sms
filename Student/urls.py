from django.urls import path

from Student import views

urlpatterns =[
    path('index',views.index),
    path('readinex',views.readindex)

]