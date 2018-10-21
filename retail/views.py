from django.shortcuts import render
from django.http import HttpResponse


def home_view(response):
    return render(response, 'retail/index.html')


def updates_view(response):
    return render(response, 'retail/updates/index.html')


def promos_view(response):
    return HttpResponse('hello Promos')


def purchases_view(response):
    return HttpResponse('hello purchases')


def social_view(response):
    return HttpResponse('hello social')
