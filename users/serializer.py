from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.Serializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'is_verified']
        

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(email=validated_data['email'], password=validated_data['password'])
    