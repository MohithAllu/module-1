from django.db import models

# Create your models here.
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
from django.db import models
from django.contrib.auth import get_user_model

from django.db import models
from django.contrib.auth import get_user_model

from django.db import models
from django.contrib.auth import get_user_model

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # ForeignKey to User model

    def __str__(self):
        return self.title

