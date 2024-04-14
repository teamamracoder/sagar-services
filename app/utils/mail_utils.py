import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re


class MailUtils:

    @staticmethod
    def send(recipient_email: str, subject: str, message: str) -> bool:
        try:
            # check recipient email is valid or not
            if not MailUtils.is_valid_email(recipient_email):
                return False

            # sender email
            sender_email = "team.amracoder@gmail.com"
            sender_password = "amvh lmza omkm orrl"

            # Set up the SMTP server
            smtp_server = smtplib.SMTP("smtp.gmail.com", 587)

            # Start TLS encryption
            smtp_server.starttls()

            # Log in to your email account
            smtp_server.login(sender_email, sender_password)

            # Create a multipart message container
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = recipient_email
            msg["Subject"] = subject

            # Add the message body
            msg.attach(MIMEText(message, "plain"))

            # Send the email
            smtp_server.send_message(msg)

            # Close the connection
            smtp_server.quit()

            # return true
            return True
        except Exception as e:
            # return false
            return False

    @staticmethod
    def is_valid_email(email: str) -> bool:
        try:
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if re.match(pattern, email):
                return True
            else:
                return False
        except Exception as e:
            return False
