from django.core.exceptions import TooManyFieldsSent
from rest_framework import serializers
from .models import Watchlist
from .models import User

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Watchlist
        # user = serializers.PrimaryKeyRelatedField(
        #     # read_only=True,
        #     queryset=User.objects.all()
        #     # view_name="user_detail"
        #     )
        fields = ('id','ticker_symbol', 'name', 'current_stock_price', 'purchase_price', 'selling_price', 'purchase_date', 'percent_change', "user")

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('id','name', 'username', 'password')