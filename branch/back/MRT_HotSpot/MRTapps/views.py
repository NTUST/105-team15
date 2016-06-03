from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return HttpResponse("Hello World!")

#def get_name(request):
#    if request.method == 'POST':
#        form = NameForm(request.POST)
#
#        if form.is_valid():
#            return HttpResponseRedirect('/thanks/')
#
#    else:
#        form = NameForm()
#
#    return render(request, 'name.html', {'form':form})
