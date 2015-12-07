from django.db import models
class article(models.Model):
    title=models.CharField(max_length="50")
    author=models.CharField(max_length="50")
    public_date=models.DateField()
    catagory=models.CharField(max_length="10")
    image=models.ImageField()
    optional_image=models.ImageField()
    body_text=models.TextField()
# Create your models here.
