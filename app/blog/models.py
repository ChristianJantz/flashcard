from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.text import slugify

from django.db.models.signals import pre_save

# Create your models here.


class Post(models.Model):

    class PostStatusOptions(models.TextChoices):
        DRAFT = 'DRAFT', 'draft'
        PUBLISH = 'PUBLISH', 'publish'
        INPROGRESS = 'INPROGRESS', 'in progress'

    catagory = models.CharField(null=False, max_length=50)
    title = models.CharField(max_length=100, null=False)
    slug = models.SlugField()
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=100, default=PostStatusOptions.INPROGRESS, choices=PostStatusOptions.choices)

    def __str__(self):
        return f"{self.title}"


def pre_save_post(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    instance.slug = slug


pre_save.connect(pre_save_post, sender=Post)
