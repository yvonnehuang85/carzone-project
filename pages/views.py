from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from cars.models import Car
from pages.models import Team


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')

    # search_fields = Car.objects.values('model', 'city', 'year', 'body_type')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_type_search = Car.objects.values_list('body_type', flat=True).distinct()

    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        # 'search_fields': search_fields,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_type_search': body_type_search,
    }

    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = "There is an email subject from the website. Subject: " + subject
        message_body = "Name: " + name + "\nEmail: " + email + "\nPhone: " + phone + "\nMessage: " + message

        # get email of superuser
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        # email function
        send_mail(
            email_subject,
            message_body,
            'yvonnehang90@gmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(request, "We received your message! Please allow 3 business days for replying. Thank you! ")
        return redirect('contact')

    return render(request, 'pages/contact.html')