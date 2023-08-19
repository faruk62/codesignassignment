from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Palette(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_public = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
class PaletteColor(models.Model):
    palette = models.ForeignKey(Palette, on_delete=models.CASCADE, related_name='colors')
    color_code = models.CharField(max_length=7)  # e.g., #FFFFFF
    is_dominant = models.BooleanField(default=False)

class FavoritePalette(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    palette = models.ForeignKey(Palette, on_delete=models.CASCADE)
    
class PaletteRevision(models.Model):
    palette = models.ForeignKey(Palette, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    revision_date = models.DateTimeField(auto_now_add=True)

