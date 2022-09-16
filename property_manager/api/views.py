from django.shortcuts import render
from django.http import JsonResponse

def getRoutes(request):
    return JsonResponse('It Works', safe=False)
