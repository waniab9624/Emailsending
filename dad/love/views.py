# emails/views.py

from django.shortcuts import render
from django.core.mail import send_mail
from .models import EmailTemplate, Recipient

def send_email(request):
    if request.method == 'POST':
        template_id = request.POST.get('template_id')
        recipients = Recipient.objects.all()
        template = EmailTemplate.objects.get(id=template_id)
        subject = template.subject
        body = template.body
        recipient_list = [recipient.email for recipient in recipients]
        send_mail(subject, body, 'your_email@example.com', recipient_list)
        return render(request, 'emails/success.html')
    else:
        templates = EmailTemplate.objects.all()
        return render(request, 'emails/send_email.html', {'templates': templates})
