from django.core.mail import mail_admins

from src.apps.contact.models import Contact


def send_mail_about_new_message_to_admins_and_save_to_db(
    sender_name: str, email: str, subject: str, message: str
):
    """Messages admins and saves message to db"""
    _send_mail_about_new_message_to_admins(sender_name, email, subject, message)
    _save_user_message_to_db(sender_name, email, subject, message)


def _send_mail_about_new_message_to_admins(
    sender_name: str, email: str, subject: str, message: str
):
    """Sends predefined message about user's message to admins"""
    mail_admins(
        f"You have new message from {sender_name}",
        f"Subject:  {subject}\nEmail:  {email}\nMessage:  {message}",
        fail_silently=False,
    )


def _save_user_message_to_db(sender_name: str, email: str, subject: str, message: str):
    """Saves user's message to db"""
    contact = Contact(name=sender_name, email=email, subject=subject, message=message)
    contact.save()
