from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Changes
def index(request):
    return render(request, 'blog/index.html')

def specific(request):

    list1=[1,2,3,4]
    return HttpResponse(list1)


def getResponse(request):

    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)

