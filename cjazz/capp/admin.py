from django.contrib import admin
from .models import *
# Register your models here.

class CArtist(admin.ModelAdmin):
    list_display = [
        'name',
        'salary',
        'active',
        'joined',
    ]
    list_display_links = ['name']
    list_editable = ['active']
    search_fields = ['name']
    list_filter = ['music']

class CMusic(admin.ModelAdmin):
    search_fields = ['type']

class CPlan(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
    ]
    search_fields = ['name']

class CPros(admin.ModelAdmin):
    search_fields = ['description']
    list_filter = ['category']

class CParty(admin.ModelAdmin):
    list_display = [
        'title',
        'time',
        'date',
        'artist',
    ]
    search_fields = ['title']
    list_filter = ['artist']

class CTicket(admin.ModelAdmin):
    list_display = [
        'name',
        'party',
        'plan',
        'number',
        'total',
    ]
    readonly_fields = (
        'name',
        'email',
        'phone',
        'plan',
        'party', 
        'number', 
        'feedback',
        'total',
    )
    search_fields = ['name']
    list_filter = ['party']

class CContact(admin.ModelAdmin):
    list_display = [
        'company',
        'email',
    ]
    readonly_fields = (
        'name',
        'email',
        'company',
        'message',
    )

    search_fields = ['company']

admin.site.register(Artist, CArtist)
admin.site.register(Music, CMusic)
admin.site.register(Plan, CPlan)
admin.site.register(Pros, CPros)
admin.site.register(Party, CParty)
admin.site.register(Ticket, CTicket)
admin.site.register(Contact, CContact)
admin.site.register(About)

admin.site.site_header = 'Cairo Jazz Club'
admin.site.site_title = 'Cairo Jazz Club'