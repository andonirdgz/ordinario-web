from django.contrib import admin
from .models import Hobby


class HobbyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'updated')
    ordering = ('title', 'created', 'updated')
    search_fields = ('title',)
    date_hierarchy = ('created')


admin.site.register(Hobby, HobbyAdmin)
