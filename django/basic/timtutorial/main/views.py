from django.shortcuts import render
from django.http import HttpResponse


def index(Response):
    return HttpResponse("<p>Badru</p>")

def v1(Response):
    return HttpResponse("<p>View</p>")
