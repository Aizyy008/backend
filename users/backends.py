from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed
import base64

User = get_user_model()

class EmailBackend(ModelBackend):

    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):  # Validate password
                return user
        except User.DoesNotExist:
            return None
        return None


class EmailBasicAuthentication(BasicAuthentication):
    
    def authenticate_credentials(self, userid, password, request=None):
        try:
            user = User.objects.get(email=userid)
        except User.DoesNotExist:
            raise AuthenticationFailed("Invalid email or password.")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Invalid email or password.")
        
        if not user.is_active:
            raise AuthenticationFailed("User account is inactive.")
        
        return (user, None)