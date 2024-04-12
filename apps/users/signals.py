from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile
from apps.chat.models import Account


@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    print(instance.id, instance.username, instance.phone_number)
    if created:
        account = Account.objects.create()
        profile = UserProfile.objects.create(
            username=f"@{instance.username}",
            phone_number=instance.phone_number,
            accounts=account,
            user=instance,
        )
        print(account, profile)
