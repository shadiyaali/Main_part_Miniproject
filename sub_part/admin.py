from django.contrib import admin
from .models import image_data, userdata 

# Register your models here.
admin.site.register(userdata),
admin.site.register(image_data),