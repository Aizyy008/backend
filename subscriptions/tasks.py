# subscriptions/tasks.py

from celery import shared_task
from datetime import datetime
from .models import Subscription

@shared_task
def deactivate_expired_subscriptions():
    current_date = datetime.now().date()

    expired_subscriptions = Subscription.objects.filter(end_date__lt=current_date, is_active=True)

    for subscription in expired_subscriptions:
        subscription.is_active = False
        subscription.save()

    return f"{expired_subscriptions.count()} subscriptions deactivated."
