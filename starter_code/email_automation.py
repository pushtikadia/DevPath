# Starter code: Simple Email Automation
import smtplib
from email.mime.text import MIMEText

def send_email(sender, password, receiver, subject, body):
    """Send an email using Gmail SMTP."""
    # TODO: Create the email message
    # TODO: Connect to Gmail SMTP server
    # TODO: Login with sender credentials
    # TODO: Send the email
    pass

def read_recipients(file_path):
    """Read recipient emails from a text file."""
    # TODO: Open the file and read emails line by line
    pass

if __name__ == "__main__":
    send_email("your@gmail.com", "yourpassword", "receiver@gmail.com", "Hello", "Test message")