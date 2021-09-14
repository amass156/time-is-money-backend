from django.http import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers, viewsets
from .serializers import WatchlistSerializer
from .serializers import UserSerializer
from .models import User
from .models import Watchlist

# Create your views here.

class WatchlistView(viewsets.ModelViewSet):
    serializer_class = WatchlistSerializer
    queryset = Watchlist.objects.all()

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# # @api_view(['GET'])
# def watchList(request):
#     list = Watchlist.objects.all()
#     serilizer = WatchlistSerializer
#     serializer_class = WatchlistSerializer
#     queryset = Watchlist.objects.all()
#     data = serializer_class
#     return HttpResponse(data)

