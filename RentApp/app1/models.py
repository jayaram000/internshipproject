from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField(default="")
    image=models.ImageField(upload_to="images/category",null=True,blank=True)
    def __str__(self):
        return self.name



class Item(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to="images/item",null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    phone=models.IntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    item_status=(models.CharField(max_length=20,default="available"))
    def __str__(self):
        return self.name


class Favo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class BookingRequest(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    email = models.EmailField()
    requested_date = models.DateField()
    message = models.TextField(null=True,blank=True)
    booking_status=models.CharField(max_length=20,default="pending")
    uploadedBy = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username