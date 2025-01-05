from django.db import models
from django.contrib.auth.models import User
import random, string

class Pizza(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField(default=100)
    image=models.URLField()
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS=(
        ("Order Recieved", "Order Recieved"),
        ("Baking","Baking"),
        ("Baked","Baked"),
        ("Out of Delivery","Out of Delivery"),
        ("Order Deliverd","Order Deliverd"),
    )
    pizza=models.ForeignKey(Pizza, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    order_id=models.CharField(max_length=100,null=True, blank=True)
    amount=models.FloatField()
    status=models.CharField(max_length=100,choices=STATUS,default="Order Recieved")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.pizza} - status {self.status}"
    
    def generate_order_id(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(8))

    def save(self,*args,**kwargs):
        if not self.pk:
            self.order_id=self.generate_order_id()
        super(Order,self).save(*args,**kwargs)

