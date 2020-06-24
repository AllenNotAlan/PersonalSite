from django.db import models
from django.contrib.auth.models import User
from PIL import Image #library to resize images and more

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #cascade = if user deleted, so will profile
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') #upload to, uploads images to folder "profile_pics"

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs) #args and kwargs added to fix error

    #     #resizes the image when uploaded
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)