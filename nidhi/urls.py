"""
URL configuration for nidhi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from website.views import (
    home, about, room, amenities, contact, booking_page, booking_form,
    register, login_user, logout_user, login as login_page,
    contact_form, hotel_list
)

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('room/', room, name='room'),
    path('amenities/', amenities, name='amenities'),

    path('booking/', booking_page, name='booking'),
    path('booking-form/', booking_form, name='booking_form'),

    # Auth
    path("register/", register, name="register"),
    path("login/", login_page, name="login"),
    path("login-user/", login_user, name="login_user"),
    path("logout/", logout_user, name="logout"),

    # Contact
    path('contact/', contact, name='contact'),
    path("contact-form/", contact_form, name="contact_form"),

    # Hotels (Admin added - display only)
    path('hotels/', hotel_list, name='hotel_list'),
]


# ✅ Media config MUST be at end
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
