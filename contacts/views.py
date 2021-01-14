from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
from contacts.models import Contact


def inquiry(request):
    # get value from the form (html)
    if request.method == "POST":
        car_id = request.POST["car_id"]
        car_title = request.POST["car_title"]
        user_id = request.POST["user_id"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        customer_need = request.POST["customer_need"]
        city = request.POST["city"]
        state = request.POST["state"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        if request.user.is_authenticated:
            user_id = request.user.id
            contactBefore = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if contactBefore:
                messages.error(request, "You have already contacted for this car before, please wait 3 business days for replying.")
                return redirect("/cars/" + car_id)

        # models (store in database)
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name,
                          customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)

        # get email of superuser
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        # email function
        send_mail(
            # subject
            'New Car Inquiry',
            # message
            'You have an inquiry for '+ car_title + 'Please log in to check',
            # EMAIL_HOST_USER
            'yvonnehang90@gmail.com',
            [admin_email],
            fail_silently=False,
        )


        contact.save()
        messages.success(request, "Your request is successfully submitted! Please allow 3 business days for replying.")
        return redirect("/cars/" + car_id)
