from django.shortcuts import render
from home import models

def displayData(request):
    datas = models.TestData.objects.all()
    context = {
    'datas': datas
    }
    return render(request,"home/display.html",context)
