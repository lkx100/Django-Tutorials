from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    

# One to Many

class chaiReviews(models.Model):
    RATING_CHOICES = [
        ('1', 'Poor'),
        ('2', 'Not Good'),
        ('3', 'Average'),
        ('4', 'Good'),
        ('5', 'Excellent')
    ]
    chai = models.ForeignKey(chaiVariety, on_delete = models.CASCADE, related_name = 'reviews')
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    rating = models.CharField(max_length = 1, choices = RATING_CHOICES)
    comment = models.TextField(max_length = 200)
    date_added = models.DateField()

    def __str__(self):
        return f"{self.user.username} review for {self.chai.name}"
    
# Many to Many

class Store(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    chai_variety = models.ManyToManyField(chaiVariety, related_name = 'stores')

    def __str__(self):
        return self.name
    
# One to One

class chaiCertificate(models.Model):
    chai = models.OneToOneField(chaiVariety, on_delete = models.CASCADE, related_name = 'certificate')
    certificate_id = models.CharField(max_length = 100)
    issue_date = models.DateField()
    valid_until = models.DateField()

    def __str__(self):
        return f"Certificate for {self.name.chai}"