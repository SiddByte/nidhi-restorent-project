from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Booking

def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def room(request):
    return render(request, 'website/room.html')

def amenities(request):
    return render(request, 'website/amenities.html')

def booking_page(request):
    return render(request, 'website/booking.html')

def login(request):
    return render(request, 'website/login.html')

def contact(request):
    return render(request, 'website/contact.html')


# AJAX FORM SAVE
def booking_form(request):
    if request.method == "POST":
        Booking.objects.create(
            fname=request.POST.get("fname"),
            lname=request.POST.get("lname"),
            mobile=request.POST.get("mobile"),
            email=request.POST.get("email"),
            check_in=request.POST.get("date_1"),
            check_out=request.POST.get("date_2"),
            request=request.POST.get("request"),
        )
        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"})


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# REGISTER
def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        cpassword = request.POST.get("cpassword")

        if password != cpassword:
            messages.error(request, "Passwords do not match")
            return redirect("login")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered")
            return redirect("login")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name
        )
        user.save()

        messages.success(request, "Registration successful. Please login.")
        return redirect("login")

    return redirect("login")


# LOGIN
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")

    return redirect("login")


# LOGOUT
def logout_user(request):
    logout(request)
    return redirect("home")


def login(request):
    return render(request, 'website/login.html')


from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Contact
from django.conf import settings

def contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save to DB
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        # Send Email
        full_message = f"""
        New Contact Form Submission:

        Name: {name}
        Email: {email}
        Subject: {subject}
        Message: {message}
        """

        send_mail(
            subject=f"New Contact Form Submission: {subject}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],  # jaha mail receive karna hai
            fail_silently=False,
        )

        return JsonResponse({"status": "success"})

    return JsonResponse({"status": "error"})




from django.shortcuts import render
from .models import Hotel

def hotel_list(request):
    hotels = Hotel.objects.all().order_by('-id')
    return render(request, 'website/hotel_list.html', {'hotels': hotels})

def room(request):
    hotels = Hotel.objects.all().order_by('-id')
    return render(request, "website/room.html", {"hotels": hotels})

def room_home(request):
    hotels = Hotel.objects.all().order_by('-id')
    return render(request, "website/index.html", {"hotels": hotels})
