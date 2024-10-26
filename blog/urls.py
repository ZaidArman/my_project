from django.urls import path
from . import views

# Changes
urlpatterns = [
    path('',views.index, name='index'),
    path('specific',views.specific,name='specific'),
    path('getResponse',views.getResponse,name='getResponse')


]