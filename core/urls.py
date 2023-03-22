from . import views
from django.urls import include, path

urlpatterns = [
    path('',views.frontpage,name='frontpage'),
    path('about/',views.aboutpage,name='about')
] 
