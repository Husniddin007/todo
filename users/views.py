from datetime import datetime, timedelta

from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .models import UserAuth, User
from .serializers import UserAuthSendCodeSerializer, UserAuthConfirmSerializer, UserSerializer
from .sms_code_validate import generate_sms_code


class UserAuthSendCodeView(APIView):

    def post(self, request):
        serializer = UserAuthSendCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_nuber = serializer.validated_data['phone_number']
        # logics to send code

        generated_code = generate_sms_code()
        serializer.save(
            sms_code=generated_code
        )
        return Response(status=status.HTTP_200_OK)


class UserAuthConfirmCodeView(APIView):

    def post(self, data):

        sended = timezone.now() - timedelta(minutes=10)

        serializer = UserAuthConfirmSerializer(data=data.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        sms_code = serializer.validated_data['sms_code']

        user_auth = UserAuth.objects.filter(
            phone_number=phone_number,
            confirmed=False
        ).last()
        sent_at = user_auth.sent_at
        if not user_auth:
            return Response({"msg": "User auth topilmdi"})
        if sent_at < sended:
            return Response({"msg": "Vaqt tugadi"})
        if sms_code != user_auth.sms_code:
            return Response({"msg": "Kod noto`g`ri"})
        user = User.objects.create_user(
            username=f'user_{phone_number}',
            phone_number=phone_number
        )
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        user_data = UserSerializer(user).data

        return Response(
            {
                'refresh': str(refresh),
                'access': str(access),
                'user': user_data
            }
        )
