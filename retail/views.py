from django.shortcuts import render
from django.http import HttpResponse

from retail.models import AmazonReviews
from retail.models import Products

def home_view(response):
    #reviews_list = AmazonReviews.objects.all()
    #return render(response, 'retail/index.html', context={'reviews_list': reviews_list[:5]})
    product_list = Products.objects.all()
    return render(response, 'retail/index.html', context={'product_list': product_list})

def updates_view(response):
    return render(response, 'retail/updates/index.html')


def promos_view(response):
    return render(response, 'retail/promos/index.html')


def purchases_view(response):
    return render(response, 'retail/purchases/index.html')


def social_view(response):
    return render(response, 'retail/social/index.html')
