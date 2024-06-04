from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage
def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            middle_name = form.cleaned_data["middle_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            date_of_birth = form.cleaned_data["date_of_birth"]
            phone_number = form.cleaned_data["phone_number"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            Form.objects.create(first_name=first_name, middle_name=middle_name, last_name=last_name,
                                email=email, address=address, date_of_birth=date_of_birth, phone_number=phone_number,
                                date=date, occupation=occupation)

            message_body = (f"Hi {first_name}, \n\nThanks for your application for the Python Developer position! We'll review it soon and be in touch within [timeframe]. \n\nBest, \n\nThe Hiring Team.")
            email_message = EmailMessage(f"Thanks for Applying, {first_name} {middle_name} {last_name}!", message_body, to=[email])
            email_message.send()

            messages.success(request,"Form submitted successfully!")

    return render(request, "index.html")


def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")



