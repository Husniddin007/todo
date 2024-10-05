from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserAuthSendCodeSerializer, UserAuthConfirmSerializer
from .sms_code_validate import generate_sms_code


class UserAuthSendCodeView(APIView):

    def post(self, request):
        serializer = UserAuthSendCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_nuber = serializer.validated_data['phone_nuber']
        # logics to send code

        generated_code = generate_sms_code()
        serializer.save(
            sms_code=generated_code
        )
        return Response(status=200)


# class UserAuthConfirmCodeView(APIView):
#
#     def post(self, request):
#         serializer = UserAuthConfirmSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#
#         phone_number = serializer.validated_date['phone_number']
