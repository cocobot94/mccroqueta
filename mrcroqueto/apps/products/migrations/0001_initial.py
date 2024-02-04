# Generated by Django 5.0.1 on 2024-01-28 06:32

import apps.products.models
import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('category_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='products.categoryproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('cant', models.IntegerField(default=0)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_orders', to=settings.AUTH_USER_MODEL)),
                ('order_detail', models.ManyToManyField(to='products.orderdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('state', models.BooleanField(default=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to=apps.products.models.custom_upload_to)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('menu', models.CharField(blank=True, choices=[('breakfast', 'BREAKFAST'), ('lunch', 'LUNCH'), ('dinner', 'DINNER'), ('happy_hour', 'HAPPY_HOUR'), ('all_day', 'ALL_DAY')], max_length=50, null=True)),
                ('category_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
    ]
