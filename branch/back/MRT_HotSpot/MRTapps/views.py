from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from MRTapps.models import HotSpot, MRTStops, MRTLines
import os
# Create your views here.
def index(request):
    return render_to_response('home.html', locals())



def MRT(request):
    COLOR = {
        '文湖線': 'brown',
        '淡水信義線': 'red',
        '松山新店線': 'green',
        '中和新蘆線': 'yellow',
        '板南線': 'blue',
    }

    #List
    views = []
    foods = []

    #Get stopName
    stopName = request.path.split('/')[-1]

    #Get stop model
    stop = MRTStops.objects.get(stop_name = stopName)

    #Get stop line
    line = stop.stop_line.all()[0]



    #get HotStop in stop
    all_hot_spot = stop.hotspot_set.all()
    for spot in all_hot_spot :
        if spot.spot_type == '景點':
            views.append(spot)
        elif spot.spot_type == '美食':
            foods.append(spot)


    return render_to_response('MRT.html', {'stop': stopName, 'views': views, 'foods': foods, 'color': COLOR[str(line)]})




def Super(request):
    path = '../index/'

    lineNames = []
    stopNames = []
    success = []

    for i in MRTLines.objects.all():
        lineNames.append(str(i))

    for line in lineNames:
        Line = MRTLines.objects.get(line_name = line)
        for stop in os.listdir(path + line):
            sc = MRTStops.objects.filter(stop_name = stop)
            if sc.count() > 0:
                Stop = MRTStops.objects.get(stop_name = stop)
            else:
                Stop = MRTStops(stop_name = stop)
                Stop.save()
            Stop.stop_line.add(Line)

    return HttpResponse(str(MRTStops.objects.all()))
