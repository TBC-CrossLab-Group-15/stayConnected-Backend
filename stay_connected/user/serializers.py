import re
from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        write_only=True,
        error_messages={"required": "Username is required."}
    )

    password = serializers.CharField(
        write_only=True,
        min_length=8,
        error_messages={
            "required": "Password is required.",
            "min_length": "Password must have at least 8 symbols.",
        },
    )
    confirm_password = serializers.CharField(
        write_only=True,
        error_messages={"required": "Password confirm is required."},
    )
    first_name = serializers.CharField(
        min_length=2,
        error_messages={
            "required": "First name is required.",
            "min_length": "Length of this field should be at least 2 symbols.",
        },
    )
    last_name = serializers.CharField(
        min_length=3,
        error_messages={
            "required": "Last name is required.",
            "min_length": "Length of this field should at least be 3 symbols.",
        },
    )
    email = serializers.EmailField(
        error_messages={
            "required": "E-mail field is required.",
            "invalid": "Please enter a valid E-mail address.",
        }
    )

    class Meta:
        model = User
        fields = ('username', 'id', 'first_name', 'last_name', 'email', 'password', 'confirm_password')

    def validate_first_name(self, value):
        if not re.match(r'^[A-Za-z]+$', value):
            raise serializers.ValidationError("First name must only consist of latin letters.")
        return value

    def validate_last_name(self, value):
        if not re.match(r'^[A-Za-z]+$', value):
            raise serializers.ValidationError("Last name must only consist of latin letters.")
        return value

    def validate_password(self, value):
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', value):
            raise serializers.ValidationError(
                "Password should consist of at least 8 symbols, including at least one uppercase letter, one number and one special character"
            )
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords are not matching."})
        return data

    def create(self, validated_data):
        # Remove confirm_password from validated_data
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')