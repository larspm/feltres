from django.contrib import admin

# Register your models here.
from .models import Stevne, Start

admin.site.register(Stevne)
admin.site.register(Start)
