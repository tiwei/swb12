from django.contrib import admin
from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'country', 'city'),
            'description': ('<strong>UserProfile attributes</strong>'),
        }),
    )
    list_display = (
        'user',
        'country',
        'city',
    )

admin.site.register(UserProfile, UserProfileAdmin)
