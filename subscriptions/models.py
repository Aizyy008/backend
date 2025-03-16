from datetime import date, timedelta
from django.db import models
from users.models import CustomUser

PLAN_CHOICES = [
    ('Basic', 'Basic Plan'),
    ('Premium', 'Premium Plan'),
]

class Subscription(models.Model):
    plan_type = models.CharField(max_length=8, choices=PLAN_CHOICES)
    start_date = models.DateField(auto_now_add=True)
    duration = models.IntegerField(default=30)  # Duration in days
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.end_date:
            self.end_date = self.start_date + timedelta(days=self.duration)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.plan_type} Subscription ({'Active' if self.is_active else 'Expired'})"

    
class UserSubscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="subscriptions")
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="subscribers")
    is_subscribed = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.user.email} - {self.subscription.plan_type} ({'Subscribed' if self.is_subscribed else 'Not Subscribed'})"
