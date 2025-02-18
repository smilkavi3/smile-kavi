from .import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home"),
    path("getTask/",views.getTask),
    path("datas/",views.datas)
   
]
