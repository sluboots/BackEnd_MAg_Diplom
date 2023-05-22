from django.contrib import admin

from .models import Heart, Type_Heart_Disease

class HeartAdmin(admin.ModelAdmin):
    list_display = ('age', 'sex', 'cp', 'disease_type')
    list_display_links = ('cp', 'disease_type')
    search_display = ('age', 'sex', 'disease_type')

admin.site.register(Heart, HeartAdmin)
admin.site.register(Type_Heart_Disease)

# Register your models here.
