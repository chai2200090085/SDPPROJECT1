from django.db import models
from .forms import *
# Create your models here.
from django.db import models
class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    class meta:
        db_tables="Register"

class PieChartForm(forms.Form):
    y_values = forms.CharField(label='Y Values', help_text='Enter comma-separated values')
    labels = forms.CharField(label='Labels', help_text='Enter comma-separated labels')
class Feedbackformde(models.Model):
    Firstname=models.TextField(max_length=200)
    Lastname=models.TextField(max_length=200)
    Email=models.EmailField(primary_key=True)
    Comments=models.TextField(max_length=200)
    class Meta:
        db_table = "Feedbackformde"

