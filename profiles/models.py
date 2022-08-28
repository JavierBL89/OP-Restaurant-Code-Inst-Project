from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Userprofile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100)

    def __string__(self):
        return self.user.username


def create_or_update_user_profile(sender, instance, created, **args):
    """
    Create or update if exists the user profile
    """
    if created:
        Userprofile.objects.create(user=instance)
    # Existing users: just have the profile
    instance.userprofile.save()