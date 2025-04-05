from django.urls import path

from telegram.views import (
    TelegramUserRetrieveApi, TelegramUserRoleUpdateApi, TelegramUserUpsertApi,
)


app_name = 'telegram'
urlpatterns = [
    path(r'users/', TelegramUserUpsertApi.as_view(), name='user-create'),
    path(
        r'users/<int:user_id>/',
        TelegramUserRetrieveApi.as_view(),
        name='user-retrieve',
    ),
    path(
        r'users/<int:user_id>/roles/',
        TelegramUserRoleUpdateApi.as_view(),
        name='user-role-update',
    ),
]
