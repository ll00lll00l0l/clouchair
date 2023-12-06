from django.db import models
from django.contrib.auth.models import User



# Create your models here.

    
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/img', null=True, default=None)
def __str__(self):
        return self.name
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/img2')
    quantity = models.PositiveIntegerField(default=1)
def __str__(self):
        return self.name
def __str__(self):
        return f"{self.product.name} - {self.quantity}"