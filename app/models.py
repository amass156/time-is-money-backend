from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

class Watchlist(models.Model):
    ticker_symbol = models.CharField(max_length=5)
    name = models.CharField(max_length=250)
    current_stock_price = models.IntegerField
    purchase_price = models.IntegerField
    selling_price = models.IntegerField
    purchase_date = models.DateField
    percent_change = models.DecimalField
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')