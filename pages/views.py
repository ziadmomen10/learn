from typing import Text
from django.shortcuts import render
from django.db import models
from .models import PeriodDate
from datetime import date, timedelta
from datetime import datetime
from datetime import date
import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from django.db.models import Count, F, Value
import time
from .serializers import PeriodDateSerializer


# Create your views here.


#def index(request):

    #start = datetime.strptime("01-12-2021", "%d-%m-%Y")
    #date_generated = pd.date_range[(start, periods=10)]
  
    #return render(request, 'pages/index.html',{'date':date_generated.strftime("%d-%m-%Y") })


#def about(request):
    #pass

#def index(request):
    #d1 = date(2022,8,15)
    #d2 = d1 + timedelta(days=9)
    #dd = [str(d1 + timedelta(days=x)) for x in range((d2-d1).days + 1)]
    #for d in dd:
        #DL = [d]
    #return render(request, 'pages/index.html',{'date':dd})

#def events(request):
    #today = date(2022,3,15)
    #weekday = today.weekday()
    #start_delta = timedelta(days=weekday)
    #start_of_week = today - start_delta
    #week_dates = []
    #for i in range(9):
        #week_dates.append(start_of_week + timedelta(days=i))
    #return render(request, 'pages/index.html', {
        #'week_dates': week_dates,
    #})
    
    
def count(request):
    
    counter = PeriodDate.objects.all()
    
    return render(request,'pages/count.html',{'counter':counter})

class Jason_Job(viewsets.ModelViewSet):
        queryset = PeriodDate.objects.all()
        serializer_class = PeriodDateSerializer


#calender comment
@api_view(['GET','PUT'])
def CalendarCount(request):

    if request.method == 'PUT':
        serlializer = PeriodDateSerializer(data=request.data)
        if serlializer.is_valid():
            serlializer.save()
        return  Response(serlializer.data)


    elif request.method == 'GET':
    #Taking date
    
        Slected_date = str(PeriodDate.objects.last())
        #Change data type from Str into Date
        First_date= datetime.strptime(Slected_date,'%Y-%m-%d')
        #Making a list to store dates after the for loop
        dd = []
        #A loop to count 9 days after the First_date
        for i in range(10):
            a_date = (First_date + timedelta(days = i))
            #changing Date form to show the day only
            a_date = a_date.strftime('%d')
            #store results into the dd list
            dd.append(a_date)
            
            #str(dd.append(d1 + timedelta(days=i)))
        return Response(dd)

#@api_view(['POST'])
#def form(request):
   #serlializer = PeriodDateSerializer(data=request.data)
    #if serlializer.is_valid():
        #serlializer.save()
    #return  Response(serlializer.data)
