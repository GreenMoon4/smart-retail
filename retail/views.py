from django.shortcuts import render
from django.http import HttpResponse


def home_view(response):
    return render(response, 'retail/index.html')
