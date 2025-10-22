# email_utils.py
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', 'noreply@joliemimi.ie')

def send_email(subject, message, recipient_list):
    sg = SendGridAPIClient(api_key=SENDGRID_API_KEY)
    for recipient in recipient_list:
        email = Mail(
            from_email=DEFAULT_FROM_EMAIL,
            to_emails=recipient,
            subject=subject,
            plain_text_content=message,
        )
        sg.send(email)
