from django.db import models

# Create your models here.
class User(models.Model):
    username= models.CharField('User',max_length=100)
    password = models.CharField('Password',max_length=50)
    def __str__(self):
        return self.username


class Expense (models.Model):
    expense=models.CharField('Description',max_length=100)
    value=models.FloatField()
    date=models.DateField()
   
    def __str__(self):
        return self.expense

