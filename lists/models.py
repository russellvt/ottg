from django.db import models

'''
Models

Ref:
 - https://docs.djangoproject.com/en/5.1/ref/models/fields/
'''

# Create your models here.
class Item(models.Model):
    '''Item Table

    TODO:
     * Display multiple items in the table
     * Support mode than one list!
    '''
    text = models.TextField(default="")
