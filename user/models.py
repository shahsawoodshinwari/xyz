"""model layer of the user application"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """User profile model"""

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="user/images/")

    profiles = models.Manager()

    def get_profile_picture(self):
        """returns the profile picture of the user"""
        return self.picture

    def get_user(self):
        """returns the user of the profile"""
        return self.user

    def __str__(self):
        """returns the string representation of this profile"""
        return f"{self.user.get_username()}"
