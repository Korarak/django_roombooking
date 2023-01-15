from django.db import models

# Create your models here.
class bookingdata(models.Model):
    book_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=100,null=True)
    room_go = models.CharField(max_length=100,null=True)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    book_detail = models.CharField(max_length=100,null=True)
    book_user = models.CharField(max_length=100,null=False)
    book_tel =models.CharField(max_length=12,null=False)

class roomdata(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=100,null=False)

class userchk(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_fname = models.CharField(max_length=100,null=False)
    user_lname = models.CharField(max_length=100,null=False)
    user_idcard = models.CharField(max_length=13,null=False)
    user_phone = models.CharField(max_length=12,null=False)
