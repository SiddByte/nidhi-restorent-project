from django.contrib import admin
from .models import Booking
from .models import Contact

admin.site.register(Contact)

admin.site.register(Booking)
