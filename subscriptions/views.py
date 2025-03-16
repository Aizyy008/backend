from datetime import datetime, timedelta
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import CustomUser
from .models import Subscription, UserSubscription
from .serializer import SubscriptionSerializer, UserSubscriptionSerializer
from users.serializer import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from rest_framework.views import APIView


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def subscribe(request):
    try:
        user = request.user  # Get the current authenticated user
        plan_type = request.data.get("plan_type")  # Plan type passed in request data

        if not plan_type:
            return Response({"error": "Plan type is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the user already has an active subscription
        if UserSubscription.objects.filter(user=user, is_subscribed=True).exists():
            return Response({"error": "You already have an active subscription."}, status=status.HTTP_400_BAD_REQUEST)

        # Retrieve the subscription object corresponding to the selected plan_type
        subscription = Subscription.objects.filter(plan_type=plan_type).first()

        if not subscription:
            return Response({"error": "Subscription plan not found."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a UserSubscription instance to link the user with the subscription
        user_subscription = UserSubscription.objects.create(
            user=user,
            subscription=subscription,
            is_subscribed=True
        )

        return Response({
            "message": f"Successfully subscribed to {subscription.plan_type} plan.",
            "subscription": {
                "plan_type": subscription.plan_type,
                "duration": subscription.duration,
                "start_date": subscription.start_date,
                "end_date": subscription.end_date
            }
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def unsubscribe(request):
    try:
        user = request.user  # Get the current authenticated user

        # Get the active user subscription
        user_subscription = UserSubscription.objects.filter(user=user, is_subscribed=True).first()

        if not user_subscription:
            return Response({"error": "You don't have an active subscription to unsubscribe from."}, status=status.HTTP_400_BAD_REQUEST)

        # Mark the user as unsubscribed
        user_subscription.is_subscribed = False
        user_subscription.save()

        return Response({
            "message": "You have successfully unsubscribed from the plan."
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

CustomUser = get_user_model()

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_profile(request):
    try:
        user = request.user  
        print(f"Authenticated User: {user.email} (ID: {user.id})")

        # Fetch the active subscription for the user
        user_subscription = UserSubscription.objects.filter(user=user, is_subscribed=True).select_related('subscription').first()

        # Serialize and return only subscription details and subscription status
        return Response({
            "subscription": UserSubscriptionSerializer(user_subscription).data if user_subscription else None
        }, status=status.HTTP_200_OK)

    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['GET'])
@permission_classes([IsAdminUser])
def get_expired_subscriptions(request):
    try:
        expired_subscriptions = Subscription.objects.filter(end_date__lt=now().date(), is_active=True)
        expired_subscriptions.update(is_active=False)

        return Response(SubscriptionSerializer(expired_subscriptions, many=True).data)

    except ObjectDoesNotExist:
        return Response({"error": "No expired subscriptions found"}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@authentication_classes([JWTAuthentication]) 
@permission_classes([IsAuthenticated]) 
def getAllSubscriptionPlans(request):
    try:
        subscription_plans = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscription_plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)