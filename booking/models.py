from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    bio = models.CharField(max_length=90)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username
