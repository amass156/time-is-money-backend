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
    current_stock_price = models.DecimalField(max_digits=10, decimal_places=2, default=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, default=True)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, default=True)
    purchase_date = models.DateField(default=True)
    percent_change = models.DecimalField(max_digits=10, decimal_places=2, default=True)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='watchlist')