from rest_framework import serializers
from users.models import User, UserAuth


class UserAuthSendCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = [
            'name',
            'phone_nuber',
            'sms_code',
            'confirmed',
            'sent_at',
        ]

    def validate_phone_number(self, phone_number):
        if User.objects.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError('Allaqachon bor')
        return phone_number

class UserAuthConfirmSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=50)
    sms_code = serializers.CharField(max_length=4)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'name',
            'phone_number', ]
