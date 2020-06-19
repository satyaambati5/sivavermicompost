from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail as sm
from django.conf import settings
# Create your views here.


def home(request):
    return render(request, "index.html",)
    # return render(request,"index.html")


def send(request):
    name = str(request.POST["your-name"])
    email = str(request.POST["your-email"])
    number = int(request.POST["phone"])
    message = str(request.POST["message"])
    num = str(number)
    if len(num) < 10:
        return HttpResponse(f"Please Eenter A Valid Mobile Number.")
    res = sm(
        subject=email,
        message=message + "\n CONTACT:" + str(number),
        from_email=email,
        recipient_list=['ambatisathya123@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse(f"Your Email Was Successfully Received By Our Manager, We Will Contact You Shortly. THANK YOU FOR VISITING Have A Nice Day")

    # email_from = email
    # # settings.EMAIL_HOST_USER
    # recipient_list = ['ambatisathya123@gmail.com', ]
    # send_mail(name, message, email_from, recipient_list)

    # return render(request, "index.html")
