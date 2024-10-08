from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class course(models.Model):
    image=models.ImageField(upload_to='image/')
    coursename=models.CharField(max_length=50)
    description=models.TextField()          
    price=models.IntegerField()
    auther=models.CharField(max_length=25)

class Account(User):
    
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=100)



class cart_item(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Courses=models.ForeignKey(course,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)

    
