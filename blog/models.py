from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    text=models.TextField()
    created_date=models.DateField()
    published_date=models.DateField()
    def publish(self):
        self.published_date=timezne.now()
        self.save()
    def __str__(self):
        return self.title
