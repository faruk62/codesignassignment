from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Palette)
admin.site.register(PaletteColor)
admin.site.register(FavoritePalette)
admin.site.register(PaletteRevision)