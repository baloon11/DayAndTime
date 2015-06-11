# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from application.models import DayAndTime
import datetime

def check_day_time(ins):
    marked_several_days=0
    week_list=[ [ins.mon,0],[ins.tue,1],[ins.wed,2],
                [ins.thu,3],[ins.fri,4],[ins.sat,6],[ins.sun,6] ]

#if in the instance marked several days- return False
    for day in week_list:
        if day[0]==True:
            marked_several_days+=1
        if marked_several_days>1:
            return False

# This part of the function works
# only if the instance of the model has
# marked only one day
    for day in week_list:
        time=datetime.datetime.now().time()
        if day[0]==True and day[1]==datetime.datetime.today().weekday()\
                        and time>=ins.start_time and time<=ins.end_time:
            return True
    return False

def home(request):
    return render_to_response('index.html',
                                            {'inst_1':check_day_time(DayAndTime.objects.get(id=1)),
                                             'inst_2':check_day_time(DayAndTime.objects.get(id=2)),
                                             'inst_3':check_day_time(DayAndTime.objects.get(id=3)),
                                             
                                             'inst_3_start_time':DayAndTime.objects.get(id=3).start_time,
                                             'inst_3_end_time':DayAndTime.objects.get(id=3).end_time,
                                             'now':datetime.datetime.now().time()
                                             },
                              context_instance=RequestContext(request))

