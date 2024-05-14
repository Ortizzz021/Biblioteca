import os

from sendgrid.helpers.mail import Mail
from sendgrid.sendgrid import SendGridAPIClient

message = Mail(
    from_email='bibliotecajdpython@gmail.com',
    to_emails='dortizortiz021@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))