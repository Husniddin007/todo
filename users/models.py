from django.db import models

from django.contrib.auth.models import AbstractUser


class UserAuth(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    sms_code = models.CharField(max_length=4)
    confirmed = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)


class User(AbstractUser):
    name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)

# 1) auth user create sms code va user malumotlarni saqlab olish user phone bormi yoqmi tekshrish
# 2) auth user verification sms code va verify qilish - > agar to'g'ri bo'lsa user ga saqlash -> token berish jwt blan
#    login ham verify bilan
# 3) user update, delete, get current
