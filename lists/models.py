from django.db import models

'''
Models

Ref:
 - https://docs.djangoproject.com/en/5.1/ref/models/fields/
'''

# Create your models here.
class List(models.Model):
    pass


class Item(models.Model):
    '''Item Table

    TODO:
     * Support mode than one list!
    '''
    text = models.TextField(default="")
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)


