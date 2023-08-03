from django.contrib import admin
from .models import Gaim, Comments, Likes

# Register your models here.

admin.site.register(Gaim)
admin.site.register(Comments)
admin.site.register(Likes)
