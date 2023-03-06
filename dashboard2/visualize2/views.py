from django.shortcuts import render
from .models import DataData
from .serializers import DataDataSerializer
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
import requests   #install requests by pip command to import it

# Create your views here.

def GetView(request):
    if request.method == 'GET':
        posts = DataData.objects.all()
        serializer = DataDataSerializer(posts,many=True)
        return JsonResponse(serializer.data,safe=False)

def instance_details(request,pk):
    try:
        posts = DataData.objects.get(id=pk)  #model instance
    except posts.DoesNotExist:
        return HttpResponse(status=404)  #data does not exist

    if request.method == 'GET':
        serializer = DataDataSerializer(posts)
        return JsonResponse(serializer.data)

def index(request):
    response = requests.get('http://127.0.0.1:8000/details/').json()  #fetching data from database by this my own API endpoint.
    
    return render(request,'chartapp/sidebar.html',{'response':response})


def likelihood(request):
    response = requests.get('http://127.0.0.1:8000/details/').json()  #fetching data from database by this my own API endpoint.
    
    return render(request,'chartapp/likelihood.html',{'response':response})





    
