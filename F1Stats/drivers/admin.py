from django.contrib import admin

# Register your models here.
from .models import Constructor
from .models import Driver

admin.site.register(Driver)
admin.site.register(Constructor)