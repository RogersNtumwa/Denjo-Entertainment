from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from PIL import Image


class movie(models.Model):
    Action = "Action"
    Horror = "Horror"
    LoveStory = "LoveStory"
    Commed = "Commed"
    Adventure = "Adventure"
    Sci_fi = "Sci-fi"

    movie_type = [
        (Action, "Action"),
        (Sci_fi, "Sci-fi"),
        (Horror, "Horror"),
        (LoveStory, "LoveStory"),
        (Commed, "Commed"),
        (Adventure, "Adventure"),
    ]

    title = models.CharField(max_length=50)
    genre = models.CharField(
        max_length=100, choices=movie_type, default=Action)
    year_published = models.CharField(max_length=10)
    description = models.TextField()
    logo = models.ImageField(default="movie.png", upload_to='uploads/logo')
    moviefile = models.FileField(upload_to='uploads/files')
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')
    #    return reverse('home',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.logo.path)
        output_size = (150, 200)
        img.thumbnail(output_size)
        img.save(self.logo.path)


def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(generate_slug, sender=movie)
