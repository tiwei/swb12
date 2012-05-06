from .models import Skill, UserProfile, City, Country
from django.contrib import admin

class CountryAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


admin.site.register(Skill)
admin.site.register(UserProfile)
admin.site.register(City)
admin.site.register(Country, CountryAdmin)
