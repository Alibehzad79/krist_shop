from rest_framework import serializers
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model


class RegisterSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50, required=True, label="First Name")
    last_name = serializers.CharField(max_length=50, required=True, label="Last Name")
    email = serializers.EmailField(required=True, label="Email")
    password = serializers.CharField(
        required=True,
        label="Password",
        validators=[
            RegexValidator(
                regex="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",
                message="Has minimum 8 characters in length, At least one uppercase English letter, At least one lowercase English letter, At least one digit, At least one special character",
                code="Invalid_password",
            ),
        ],
    )

    def validate_email(self, value):
        value = value.lower()
        check_exist_email = get_user_model().objects.filter(email=value).exists()
        if check_exist_email:
            raise serializers.ValidationError("Email already exist.")

        return value

    def validate_password(self, value):
        pass
