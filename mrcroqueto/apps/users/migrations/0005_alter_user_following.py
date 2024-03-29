# Generated by Django 5.0.1 on 2024-02-01 17:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(limit_choices_to=models.Q(('id', models.F('id')), _negated=True), related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
