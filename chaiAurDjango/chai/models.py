from django.db import models
from django.utils import timezone

# Create your models here.
class chaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('GT', 'Green Tea'),
        ('MS', 'Masala Chai'),
        ('BT', 'Black Tea'),
        ('MC', 'Malai Chai'),
        ('GR', 'Ginger Tea')
    ]
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'chai_images/')
    date_added = models.DateField()
    chaiType = models.CharField(max_length = 2, choices = CHAI_TYPE_CHOICES)
    description = models.TextField(default = '')   # Default description will be "", This is optional

    def __str__(self):
        return self.name