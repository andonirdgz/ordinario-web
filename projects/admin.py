from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'updated')
    ordering = ('title', 'created', 'updated')
    search_fields = ('title',)
    date_hierarchy = ('created')


admin.site.register(Project, ProjectAdmin)
