import re
from rest_framework import serializers
from user.models import User



class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        write_only=True,
        error_messages={"required": "იუზერნეიმი სავალდებულოა."}
    )


    password = serializers.CharField(
        write_only=True,
        min_length=8,
        error_messages={
            "required": "პაროლის ველი სავალდებულოა.",
            "min_length": "პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო.",
        },
    )
    confirm_password = serializers.CharField(
        write_only=True,
        error_messages={"required": "პაროლის დადასტურება სავალდებულოა."},
    )
    first_name = serializers.CharField(
        min_length=3,
        error_messages={
            "required": "სახელის ველი სავალდებულოა.",
            "min_length": "სახელი უნდა იყოს მინიმუმ 3 სიმბოლო.",
        },
    )
    last_name = serializers.CharField(
        min_length=3,
        error_messages={
            "required": "გვარის ველი სავალდებულოა.",
            "min_length": "გვარი უნდა იყოს მინიმუმ 3 სიმბოლო.",
        },
    )
    email = serializers.EmailField(
        error_messages={
            "required": "ელფოსტის ველი სავალდებულოა.",
            "invalid": "გთხოვთ, შეიყვანოთ ვალიდური ელფოსტა.",
        }
    )

    class Meta:
        model = User
        fields = ('username','id', 'first_name', 'last_name', 'email', 'password', 'confirm_password')

    def validate_first_name(self, value):
        if not re.match(r'^[A-Za-z]+$', value):
            raise serializers.ValidationError("სახელი უნდა შეიცავდეს მხოლოდ ლათინურ სიმბოლოებს.")
        return value

    def validate_last_name(self, value):
        if not re.match(r'^[A-Za-z]+$', value):
            raise serializers.ValidationError("გვარი უნდა შეიცავდეს მხოლოდ ლათინურ სიმბოლოებს.")
        return value

    def validate_password(self, value):
        if not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', value):
            raise serializers.ValidationError(
                "პაროლი უნდა შეიცავდეს მინიმუმ 8 სიმბოლოს, მათ შორის ერთი დიდი და პატარა ასო, რიცხვი და სიმბოლო."
            )
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "პაროლები არ ემთხვევა."})
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