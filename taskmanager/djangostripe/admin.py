from django.contrib import admin
from .models import *

class SlugSize(admin.ModelAdmin):
    prepopulated_fields={"slug":("name",)}


admin.site.register(Item,SlugSize)
admin.site.register(Sex)
admin.site.register(Type)
admin.site.register(Size)
