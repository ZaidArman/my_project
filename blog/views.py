from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

OPENAI_API_KEY = "sk-0iGd9K1i8Ct1LZiHZiziQO-LTuk9mZul5q6DUYo4obT3BlbkFJ7_oIC91mtgFq_JIIrhPCTkX-WuC2ciO1nYCr1bK3QA"

def index(request):
    return render(request, 'blog/index.html')

def specific(request):

    list1=[1,2,3,4]
    return HttpResponse(list1)


def getResponse(request):

    userMessage = request.GET.get('userMessage')
    return HttpResponse(userMessage)

