from django.contrib import admin
from .models import Job,Category,Location,Profile

# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Profile)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("title","category","location","time")
    list_filter = ("category","location","pub_date",)
    search_fields = ["title"]

