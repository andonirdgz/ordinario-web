from django.contrib import admin
from .models import Artwork, Order


class ArtworkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'updated')
    ordering = ('title', 'created', 'updated')
    search_fields = ('title',)
    date_hierarchy = ('created')


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('created', 'name', 'total')
    ordering = ('created',)
    search_fields = ('name',)


admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Order, OrderAdmin)
