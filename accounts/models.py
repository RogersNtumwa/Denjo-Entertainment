from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg",
                              upload_to='uploads/profile_pics')

    def __str___(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        output_size = (125, 125)
        img.thumbnail(output_size)
        img.save(self.image.path)


@receiver(post_save, sender=User)
def create_profilel(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)
    instance.profile.save()
