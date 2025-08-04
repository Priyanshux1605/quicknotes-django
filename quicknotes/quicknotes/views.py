from django.http import HttpResponse 
from django.shortcuts import render

'''def home(request):
    return HttpResponse("hello, world.Its a httpresponse")
'''
def home(request):
    return render(request,'index.html')
   