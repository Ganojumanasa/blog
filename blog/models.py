from django.db import models

# Create your models here.
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, blank=True)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
