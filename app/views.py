from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'RAMANA','age':23,'hobbies':['cricket','football']}
    return render(request,'loop.html',context=d)
