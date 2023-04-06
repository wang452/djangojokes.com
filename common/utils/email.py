import sendgrid
from sendgrid.helpers.mail import Mail

from django.conf import settings


def send_email(to, subject, content, sender='admin@example.com'):
    sg = sendgrid.SendGridAPIClient(settings.SENDGRID_API_KEY)
    # override the sender and to values with values from local_settings.py file
    sender = settings.SENDER
    to = settings.RECEIVER
    mail = Mail(
        from_email=sender,
        to_emails=to,
        subject=subject,
        html_content=content
    )
    return sg.send(mail)
