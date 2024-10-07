from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>При отправке POST /HelloWorld возвращает JSON</h1>")

def HelloWorld(request):
    if request.method == "POST":
        return JsonResponse({"course": "Cloud technologies", "name": "Burmagin Daniil", "group": "BSE232"})
    else:
        return HttpResponseNotFound