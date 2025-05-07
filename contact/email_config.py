from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.conf import settings


def send_mail(to,subject,message):
    content = MIMEMultipart()

    content['from'] = settings.EMAIL_HOST_USER
    content['to'] = to
    content['subject'] = subject

    content.attach(MIMEText(message,"plain"))

    with smtplib.SMTP(host=settings.EMAIL_HOST, port=settings.EMAIL_PORT) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD)
        smtp.sendmail(
            from_addr=settings.EMAIL_HOST_USER,
            to_addrs= to,
            msg= content.as_string()
        )
        print("Done...")