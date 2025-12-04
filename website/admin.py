from django.contrib import admin
from .models import Booking
from .models import Contact
from django.contrib import admin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')


admin.site.register(Contact)

admin.site.register(Booking)
