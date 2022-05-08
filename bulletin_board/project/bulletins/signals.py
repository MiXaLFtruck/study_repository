from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from bulletins.models import Comment


@receiver(post_save, sender=Comment)
def new_comment_notification(sender, instance, created, **kwargs):
    if created:
        bulletin = instance.post
        html_content = render_to_string('email/new_comment_notification.html', {'bulletin': bulletin})
        msg = EmailMultiAlternatives(
            subject=f"{instance.post.author}, на ваше объявление поступил новый отклик!",
            body="",
            to=[instance.post.author.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
