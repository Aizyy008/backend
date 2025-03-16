from rest_framework import serializers
from .models import *

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
        
        
class UserSubscriptionSerializer(serializers.ModelSerializer):
    subscription_details = SubscriptionSerializer(source="subscription", read_only=True)

    class Meta:
        model = UserSubscription
        fields = ["subscription_details", "is_subscribed"]
