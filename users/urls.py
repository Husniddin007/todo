from django.urls import path

from users.views import UserAuthSendCodeView,UserAuthConfirmCodeView

urlpatterns = [
    path('create/', UserAuthSendCodeView.as_view(), name='create'),
    path('confirm/', UserAuthConfirmCodeView.as_view(), name='confirm'),
]