from django.contrib import admin
from .models import Booking, Kayak, Route, BookingKayaks


class BookingKayakInLine(admin.TabularInline):
    model = BookingKayaks
    raw_id_fields = ['kayak']


class BookingAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user', 'route', 'term', 'time']
    inlines = [BookingKayakInLine]

admin.site.register(Booking, BookingAdmin)


class KayakAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'type', 'available', 'description']

admin.site.register(Kayak, KayakAdmin)


class RouteAdmin(admin.ModelAdmin):
    list_display = ['name', 'distance', 'description']

admin.site.register(Route, RouteAdmin)



