from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializers import UserAuthSerializer, UserSerializer
from .models import User, UserAuth


class UserAuthCreateView(CreateAPIView):
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"massage": "User createdd"})
        return Response(serializer.errors, status=400)
