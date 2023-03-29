# views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from .models import ContactForm

# Import the MailSender class from the sendmail module
from sendmail import MailSender

@csrf_protect
def send_email(request):
    if request.method == 'POST':
        # Save the form data to the database
        name = request.POST['name']
        email = request.POST['email']
        ContactForm.objects.create(name=name, email=email)

        # Send the email
        plaintext = "Hello John, \n" \
                    "I'm just testing my new fancypants email sending system here.\n" \
                    "Adam"
        html = f"""<p>Name: {name}</p>
                   <p>Email: {email}</p>"""
        ourmailsender = MailSender('atulkumar1130@gmail.com', 'dznhvnkcgcwirdqo','atulkumar1130@gmail.com', ('smtp.gmail.com', 587))
        ourmailsender.set_message(plaintext, "Dataflowgroup mail", "sample mail", html)
        ourmailsender.set_recipients(['atulkumar1530@gmail.com'])
        ourmailsender.connect()
        ourmailsender.send_all()

        # Redirect to a thank you page
        return HttpResponseRedirect('/thank-you/')
    else:
        return render(request, 'contact.html')
