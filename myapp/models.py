from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Permission(models.Model):
    pages = models.ManyToManyField(Page)
    users = models.ManyToManyField(User)

    def __str__(self):
        # Get the names of pages associated with the permission
        page_names = ', '.join(page.title for page in self.pages.all())
        
        # Get the usernames of users associated with the permission
        user_names = ', '.join(user.username for user in self.users.all())
        
        # Concatenate the page names and user names
        return f"{page_names} : {user_names}"
