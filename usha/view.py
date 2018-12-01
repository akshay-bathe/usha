from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render (request,'home.html')
def count(request):
    data=request.GET['akshay']
    b=data.split()
    c=len(b)
    d = {}
    for i in b :
        if i in d:
            d[i] += 1
        else:
            d[i] = 1


    return render (request, 'count.html',{'a':data,'my':c,'is': d.items()})
