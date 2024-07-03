from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True)
def send_shedule_mail(self,email, date, username, title):
    try:
        subject = "Interview Schedule Notification"
        email_from = settings.EMAIL_HOST_USER
        message = (f"Dear Candidate,\n\n"
                   f"This email is to inform you about your upcoming interview.\n\n"
                   f"Company: {username}\n"
                   f"Job Title: {title}\n"
                   f"Date & Time: {date}\n\n"
                   f"Please ensure you are available for the interview at the scheduled time.\n\n"
                   f"Best regards,\n"
                   f"{username}")
        print("Email details:")
        print(f"From: {email_from}")
        print(f"To: {email}")
        print(f"Subject: {subject}")
        print("Message:")
        print(message)

        send_mail(subject, message, email_from, [email],fail_silently=True)
        print(f"Email sent successfully to {email}")
    except Exception as e:
        print(f'Error sending email: {e}')

@shared_task(bind=True)
def cancell_shedule_mail(self,email, date, username, title):
    try:
        subject = "Interview Cancellation Notice"
        email_from = settings.EMAIL_HOST_USER
        message = (f"Dear Candidate,\n\n"
                   f"We regret to inform you that your upcoming interview has been cancelled.\n\n"
                   f"Company: {username}\n"
                   f"Job Title: {title}\n"
                   f"Scheduled Date & Time: {date}\n\n"
                   f"We apologize for any inconvenience this may cause. We will reach out to you shortly to reschedule your interview.\n\n"
                   f"Thank you for your understanding.\n\n"
                   f"Best regards,\n"
                   f"{username}")

        print("Email details:")
        print(f"From: {email_from}")
        print(f"To: {email}")
        print(f"Subject: {subject}")
        print("Message:")
        print(message)
        
        # Send the email
        send_mail(subject, message, email_from, [email],fail_silently=True)
        print(f"Email sent successfully to {email}")
    except Exception as e:
        print(f'Error sending email: {e}')



@shared_task(bind=True)
def test(self):
    for i in range(10):
        print(i)
    return 'done'
