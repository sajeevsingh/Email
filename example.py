"""This example shows all necessary steps for sending a basic plain text message."""
import email

from django.core import mail

# Import the MailSender class from the sendmail module
from sendmail import MailSender
import cgi
import traceback

# First, let's create the plain text email we want to send. If you create this message manually in a Python script,
# you will have to specify newlines etc yourself. To avoid that you can write the message separately in a text file
# and then read it with your Python script.

plaintext = "Hello John, \n" \
            "I'm just testing my new fancypants email sending system here.\n" \
            "Adam"

# Next, we create the MailSender object which will handle connecting to the server, as well as composing and sending
# our email. For this, we need to enter the username, password and server address/port for a working SMTP server.
# If you have an email account with one of the major email providers (e.g. Gmail or equivalent) you can often find
# the SMTP server information online. You will also need to know which authorization type the SMTP server requires:
# SSL or TLS. The MailSender defaults to using TLS. See the Readme for more information.
# The settings used below illustrate connecting to Gmail's SMTP server using TLS.

ourmailsender = MailSender('sajeevysingh@gmail.com', 'gfcrhuduywjoveil','sajeevysingh@gmail.com', ('smtp.gmail.com', 587))

# We can now set the body of the message. For this, we will use your previously created plain text message.
# We will also add a subject for our email and specify the name of the sender (the 'From' name). Both the subject
# and the sender's name can also be set individually later, or be left blank. Some servers only accept specific formats
# for the sender's name. Unaccepted formats raise an error. In that case, experiment or leave the field blank.

# html = 'C:/xampp/htdocs/sample_register'

with open(r'C:\Users\sajeevsingh_dataflow\Downloads\Email_automation\sendmail-master\sample_registerr.html', 'r') as f:
    html = f.read()

ourmailsender.set_message(plaintext, "Dataflowgroup", "sample mail", html, "example.txt", "example.txt")

# Next, we set the recipient for our email. The recipients are always entered as a list (or tuple) even when
# there is only one recipient
l = [['sajeevsingh@dataflowgroup.com']]
for i in range(len(l)):
    ourmailsender.set_recipients(l[i])

# We're almost there! Now we just have to connect to the SMTP server using the account and address we specified when
# we created our MailSender, and send the email.

    ourmailsender.connect()
    ourmailsender.send_all()




# import requests
#
# # Replace <YOUR-EMAIL-DOMAIN> with the domain you want to use
# email_domain = "dataflowgroup.com.mailinator.com"
#
# # Get the list of emails sent to the temporary email address
# response = requests.get(f"https://api.mailinator.com/v2/domains/{email_domain}/inboxes/INBOX/messages")
#
# # Print the subject and body of each email
# for email in response.json():
#     subject = email['subject']
#     body = email['data']['parts'][0]['body']
#     print(f"Subject: {subject}\nBody: {body}\n")


# After all messages are sent, the connection to the server is automatically closed by default. For how to disable this,
# see the Readme.
# import imaplib
# import email
# import re
#
# # create an IMAP4_SSL object and login to the mailbox
# mail = imaplib.IMAP4_SSL('imap.gmail.com')
# mail.login('atulkumar1130@gmail.com', 'dznhvnkcgcwirdqo')
#
# # select the mailbox and search for unread messages
# mail.select('inbox')
# typ, data = mail.search(None, 'UNSEEN')
#
# # loop through all the unread messages
# for num in data[0].split():
#     typ, msg_data = mail.fetch(num, '(RFC822)')
#
#     # parse the email message using email.message_from_bytes()
#     msg = email.message_from_bytes(msg_data[0][1])
#     subject = msg['Subject']
#     body = None
#
#     # check if the message is multipart
#     if msg.is_multipart():
#         # loop through all the parts of the message
#         for part in msg.walk():
#             # check if the part is a plain text or HTML body
#             if part.get_content_type() == 'text/plain' or part.get_content_type() == 'text/html':
#                 # decode the part and store the body
#                 body = part.get_payload(decode=True).decode(errors='ignore')
#
#     # if the message is not multipart, it is a plain text message
#     else:
#         body = msg.get_payload(decode=True).decode(errors='ignore')
#
#     # extract form data using regular expressions
#     match = re.search(r'name="in_username" value="(.+)"', body)
#     if match:
#         username = match.group(1)
#
#     match = re.search(r'name="email" value="(.+)"', body)
#     if match:
#         email = match.group(1)
#
#     match = re.search(r'name="message" value="(.+)"', body)
#     if match:
#         message = match.group(1)
#
#     # do something with the form data (e.g. store it in a database)
#     print('username:', 'atulkumar1130@gmail.com')
#     print('email:', 'atulkumar1130@gmail.com')
#     print('message:', msg)
#
# # mark the message as read so we don't process it again
# mail.store(num, '+FLAGS', '\\Seen')
