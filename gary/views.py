from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def interface(request):
    return render(request, 'dashboard.html')

def takePicture(request):
    if request.method == 'GET':
        return HttpResponse('getting something')
    elif request.method == 'POST':
        status = request.POST['picture']
        return HttpResponse(status)
        
