from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings



def send_contact_email(contact_name, contact_email,
                       contact_comment):
    
    management_email = settings.DEFAULT_FROM_EMAIL
    
    subject = render_to_string(
        'contact/send_email/contact_email_subject.txt')

    body = render_to_string(
        'contact/send_email/contact_email_body.txt',
        {'contact_name': contact_name, 'contact_email': contact_email,
        'contact_comment': contact_comment}
    )

    send_mail(
        subject,
        body,
        management_email,
        [management_email]
    )