import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Function to send emails
def send_email(subject, message, recipient_list):
    """
    Sends an email using SendGrid.
    
    Args:
        subject (str): Subject of the email
        message (str): Body of the email
        recipient_list (list): List of recipient emails
    """
    # Replace with your verified sender email
    from_email = "k29singh@gmail.com"  # Verified sender in SendGrid
    
    for recipient in recipient_list:
        email = Mail(
            from_email=from_email,
            to_emails=recipient,
            subject=subject,
            html_content=message
        )
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(email)
            print(f"Email sent to {recipient}, Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error sending email to {recipient}: {e}")
