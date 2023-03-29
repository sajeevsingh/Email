import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.mime import MIMEText

# Set up email server and login
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('atulkumar1130@gmail.com', 'dznhvnkcgcwirdqo')

# Create message object and set email details
msg = MIMEMultipart()
msg['From'] = 'sender_email'
msg['To'] = 'recipient_email'
msg['Subject'] = 'HTML Form'

# Read HTML file and attach it to the message as text/html
with open('form.html', 'r') as f:
    html = f.read()
msg.attach(MIMEText(html, 'html'))

# Send email
server.sendmail('atulkumar1130@gmail.com', 'atulkumar1530@gmail.com', msg.as_string())

# Close the server connection
server.quit()
