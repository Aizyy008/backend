from django.contrib import admin

from subscriptions.models import Subscription, UserSubscription

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("plan_type", "start_date", "end_date", "is_active")
    list_filter = ("is_active",)
    search_fields = ("plan_type",)

@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "subscription", "is_subscribed")
    list_filter = ("is_subscribed",)
    search_fields = ("user__email", "subscription__plan_type")