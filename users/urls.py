from django.urls import path

from users.views import UserAuthSendCodeView

urlpatterns = [
    path('create/', UserAuthSendCodeView.as_view(), name='create'),
]