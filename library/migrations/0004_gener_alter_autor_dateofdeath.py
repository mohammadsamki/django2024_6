# Generated by Django 5.1.1 on 2024-10-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter your genre name', max_length=20)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='autor',
            name='dateOfDeath',
            field=models.DateField(blank=True, null=True, verbose_name='date of death'),
        ),
    ]
