from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student


@receiver(post_save, sender=Student)
def create_user(sender, instance: Student, created, **kwargs):
    if created:
        # Create a user with a username and password
        username = instance.name
        password = instance.password
        user = User.objects.create_user(username=username, password=password)
        print(f"Created user {user} for student {instance}.")
        # Save the user
        user.save()
