import smtplib
from email.mime.text import MIMEText
import os

try:
    # SMTP Configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    # Use environment variables (BEST PRACTICE)
    email_user = os.getenv("EMAIL_USER")
    email_password = os.getenv("EMAIL_PASS")

    if not email_user or not email_password:
        raise Exception("Missing EMAIL_USER or EMAIL_PASS environment variables")

    recipient_email = "recipient_email@example.com"

    # Email content
    subject = "Test Email from Python smtplib"
    body = "This is a test email sent using Python automation script."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = email_user
    msg["To"] = recipient_email

    # Connect to SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()

    # Login
    server.login(email_user, email_password)

    # Send email
    server.sendmail(email_user, recipient_email, msg.as_string())

    print("✅ Email sent successfully!")

    # Close connection
    server.quit()

except Exception as e:
    print("❌ Error occurred:", str(e))
