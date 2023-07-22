from django.db import models

class Categories(models.Model) :
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name

class Drinks (models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name + ' '+self.description

class Article (models.Model):
   
    model = models.CharField(max_length=250)
    brand = models.CharField(max_length=100)    
    description = models.TextField(max_length=20000)
    price = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=1)
    def __str__(self) -> str:
        return self.brand +' '+ self.model
    
