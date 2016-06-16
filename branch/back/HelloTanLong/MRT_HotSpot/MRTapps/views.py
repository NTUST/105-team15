from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from MRTapps.models import HotSpot, MRTStops, MRTLines
import os
# Create your views here.
def index(request):
    return HttpResponseRedirect('MRT/home')

def home(request):
    return render_to_response('home.html', {'lines': MRTLines.objects.all()})

def about(request):
    return render_to_response('about.html', {'lines': MRTLines.objects.all()})

def MRT(request, stopName):
    COLOR = {
        '文湖線': '#802727',
        '淡水信義線': '#ce0606',
        '松山新店線': 'green',
        '中和新蘆線': '#bfbf3d',
        '板南線': '#3434c5',
    }

    #List
    views = []
    foods = []
    images = []

    #Get stopName
    #stopName = request.path.split('/')[-1]

    #Get stop model
    stop = MRTStops.objects.get(stop_name = stopName)

    #Get stop line
    line = stop.stop_line.all()[0]

    #get HotStop in stop
    all_hot_spot = stop.hotspot_set.all()
    for spot in all_hot_spot :
        images = spot.spot_img_source.split(',')

        if spot.spot_type == '景點':
            views.append([spot, images])
        elif spot.spot_type == '美食':
            foods.append([spot, images])


    return render_to_response('MRT.html', {'stop': stopName, 'views': views, 'foods': foods, 'color': COLOR[str(line)], 'lines': MRTLines.objects.all()})




def Super(request):
    path = '../網站製作/'

    stopNames = []

    for i in MRTStops.objects.all():
        stopNames.append(str(i))

    return HttpResponse(str(stopNames))
