# Generated by Django 3.2.7 on 2021-09-10 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker_symbol', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=250)),
                ('current_stock_price', models.DecimalField(decimal_places=2, default=True, max_digits=10)),
                ('purchase_price', models.DecimalField(decimal_places=2, default=True, max_digits=10)),
                ('selling_price', models.DecimalField(decimal_places=2, default=True, max_digits=10)),
                ('purchase_date', models.DateField(default=True)),
                ('percent_change', models.DecimalField(decimal_places=2, default=True, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='app.user')),
            ],
        ),
    ]
