from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prices/',views.cryptoprice,name='prices'),
    path('pricelookup/',views.lookupprice, name='searchcrypto'),
]