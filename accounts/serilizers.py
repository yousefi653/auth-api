from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class RegisterSer(serializers.ModelSerializer):
    phone = serializers.CharField(required=False, allow_blank=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = UserModel
        fields = ("email", "first_name", "last_name", "phone", "password", "password2")
        extra_kwargs = {
            "password": {"write_only": True}
        }
    
    def validate(self, attrs):
        password1 = attrs.get("password")
        password2 = attrs.get("password2")
        
        if password1!=password2:
            raise serializers.ValidationError({"password": "Passwords are not match!"})
        return attrs
    
    def validate_email(self, data):
        if UserModel.objects.filter(email=data).exists():
            raise serializers.ValidationError("This email is already exists!")
        return data
    
    def create(self, validated_data):
        validated_data.pop("password2")
        return UserModel.objects.create_user(**validated_data)