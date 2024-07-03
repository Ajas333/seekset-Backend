from django.core.mail import send_mail
import random
from django.conf import settings


# def send_shedule(email, date, user, title):
#     try:
#         subject = "Interview Schedule Notification"
#         email_from = settings.EMAIL_HOST_USER
#         message = (f"Dear Candidate,\n\n"
#                    f"This email is to inform you about your upcoming interview.\n\n"
#                    f"Company: {user}\n"
#                    f"Job Title: {title}\n"
#                    f"Date & Time: {date}\n\n"
#                    f"Please ensure you are available for the interview at the scheduled time.\n\n"
#                    f"Best regards,\n"
#                    f"{user}")

#         print("Email details:")
#         print(f"From: {email_from}")
#         print(f"To: {email}")
#         print(f"Subject: {subject}")
#         print("Message:")
#         print(message)

#         send_mail(subject, message, email_from, [email])
#         print(f"Email sent successfully to {email}")
#     except Exception as e:
#         print(f'Error sending email: {e}')

def cancelMail(email, date, user, title):
    try:
        subject = "Interview Cancellation Notice"
        email_from = settings.EMAIL_HOST_USER
        message = (f"Dear Candidate,\n\n"
                   f"We regret to inform you that your upcoming interview has been cancelled.\n\n"
                   f"Company: {user}\n"
                   f"Job Title: {title}\n"
                   f"Scheduled Date & Time: {date}\n\n"
                   f"We apologize for any inconvenience this may cause. We will reach out to you shortly to reschedule your interview.\n\n"
                   f"Thank you for your understanding.\n\n"
                   f"Best regards,\n"
                   f"{user}")

        print("Email details:")
        print(f"From: {email_from}")
        print(f"To: {email}")
        print(f"Subject: {subject}")
        print("Message:")
        print(message)
        
        # Send the email
        send_mail(subject, message, email_from, [email])
        print(f"Email sent successfully to {email}")
    except Exception as e:
        print(f'Error sending email: {e}')
