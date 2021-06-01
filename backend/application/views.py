from django.shortcuts import render
from django.http import JsonResponse


def GetRoutes(request):
    return JsonResponse("Hello", safe=False)



