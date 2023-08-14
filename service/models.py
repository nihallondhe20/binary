from django.db import models
from phone_field import PhoneField
import datetime
from datetime import date, timedelta
# Create your models here.
from django.utils.crypto import get_random_string



   
class Service(models.Model):
    service_name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.service_name} {self.service_type}"
    
STATUS = [
        ("R","REQUEST_RCV"),
        ("A","REQ_ASSIGN"),
        ("P","PENDING"),("S","SOLVE"),
    ]

def default_next_5th_date():
    today = date.today()
    fifth_date = today.replace(day=5)
    if fifth_date <= today:
        next_month = today.replace(day=5, month=today.month + 1)
        return next_month
    return fifth_date



class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastnamr = models.CharField(max_length=255)
    phone = models.BigIntegerField(max_length=10)
  #  service_name = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_type = models.ForeignKey(Service, on_delete=models.CASCADE)
    comments = models.CharField(max_length=255)
    status = models.CharField(max_length=255,choices=STATUS,default="R")
    support_comment = models.CharField(max_length=255)
    request_raised = models.DateField(default=datetime.date.today)
    request_solve = models.DateField(default=default_next_5th_date)
    file = models.FileField(upload_to='uploads/',null=True)
    idss = models.AutoField(primary_key=True, unique=True)
    
    def __str__(self):
        return f"{self.firstname} {self.service_type}{self.status}"
  
  
 