# Generated by Django 2.1.5 on 2019-01-20 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='accounts.MyUser'),
        ),
    ]