from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializer import LoginSerializer, RegisterSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed



@api_view(["POST"])
@permission_classes([AllowAny])
def refresh_token(request):
    try:
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response({"error": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate new access token from the refresh token
        refresh = RefreshToken(refresh_token)
        new_access_token = str(refresh.access_token)

        return Response({"access": new_access_token}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": "Invalid or expired refresh token"}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    try:
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    try:
        data = request.data
        serializer = LoginSerializer(data=data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

        
            user = authenticate(email=email, password=password)
            if user is None:
                return Response({"error": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

        
            refresh = RefreshToken.for_user(user)

            return Response({
                "user_id": user.id,
                "user_email": user.email,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except ObjectDoesNotExist:
        return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"error": "Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)