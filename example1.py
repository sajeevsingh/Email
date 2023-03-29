import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

# Set up SMTP server and login details
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "atulkumar1130@gmail.com"
smtp_password = "dznhvnkcgcwirdqo"

# Set up email message
msg = MIMEMultipart()
msg['From'] = smtp_username
msg['To'] = "atulkumar1530@gmail.com"
msg['Subject'] = "HTML email"

html_content = """<!DOCTYPE html>
<html>
<head>
	<title>Contact Form</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Contact Us</h1>

<form method="post" action="action_page.php">
	<label for="name">Name:</label><br>
	<input type="text" id="name" name="name" required><br><br>

	<label for="email">Email:</label><br>
	<input type="email" id="email" name="email" required><br><br>

	<label for="message">Message:</label><br>
	<textarea id="message" name="message" required></textarea><br><br>

	<input type="submit" value="Submit">
	<input type="reset" value="Reset">
</form>

</body>
</html>

"""

msg.attach(MIMEText(html_content, 'html'))

# Connect to SMTP server and send email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(smtp_username, msg['To'], msg.as_string())

# Receive response email
# In the response handler script at 'http://your-website.com/response-handler'
# You can collect the form data and send a response email back to the user
# using the smtplib module as shown above.


from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)


@app.route('/response-handler', methods=['POST'])
def response_handler():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Set up SMTP server and login details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "atulkumar1130@gmail.com"
    smtp_password = "dznhvnkcgcwirdqo"

    # Set up email message
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = email
    msg['Subject'] = "Form Submission Received"

    body = f"Dear {name},\n\nThank you for your message.\n\nYour message: {message}"

    msg.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, email, msg.as_string())

    return "Thank you for your submission. You will receive an email response shortly."


if __name__ == '__main__':
    app.run()
