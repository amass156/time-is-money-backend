from django.contrib import admin

# Register your models here.
from .models import Watchlist
from .models import User

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('ticker symbol', 'name', 'current stock price', 'purchase price', 'selling price' 'purchase date', 'percent change', 'user')

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'password')

admin.site.register(User)
admin.site.register(Watchlist)