from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('updates/', views.updates_view, name='updates'),
    path('promos/', views.promos_view, name='promos'),
    path('purchases/', views.purchases_view, name='purchases'),
    path('social/', views.social_view, name='social'),
]
