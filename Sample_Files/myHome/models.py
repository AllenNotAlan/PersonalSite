from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # one to many relationship
from django.urls import reverse
from PIL import Image

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default='project_thumbnails/defaultProject.jpg', upload_to='project_thumbnails')
    date_posted = models.DateTimeField(default=timezone.now)
    language = models.CharField(max_length=100, blank=True)

    def __str__(self, *args, **kwargs):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})