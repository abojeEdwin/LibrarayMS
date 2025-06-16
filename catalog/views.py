from django.http import HttpResponse
from django.shortcuts import render

def get_books(request):
    return HttpResponse("Hello, world. You're at the books page.")

# Create your views here.
def greet(request,name):
    return render(request,'index.html',{'name':name})