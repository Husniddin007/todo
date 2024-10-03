import random
from twilio.rest import Client
from rest_framework import serializers
from users.models import User, UserAuth


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserAuthSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserAuth
        fields = '__all__'

    def create(self, validated_data):
        user = UserAuth(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.is_active = False
        user.save()
        verification_code = str(random.randint(1000, 9999))
        phone_number = validated_data.get['phone_number']
        UserAuth.objects.create(user=user, phone_number=phone_number, verification_code=verification_code)
        self.send_verification_sms(phone_number, verification_code)
        return user

    def send_verification_sms(self, phone_number, verification_code):
        account_sid = 'US881c150986e2d349516c9c39ee70f3c3'
        auth_token = '2XMVNY93LA98JGHTX5LAPUFB'
        twilio_number = +998901579767

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f' sms {verification_code}',
            from_=twilio_number,
            to=phone_number
        )
        return message
