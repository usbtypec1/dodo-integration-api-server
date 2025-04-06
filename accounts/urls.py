from django.urls import path

from accounts.views import AccountTokenRetrieveApi


urlpatterns = [
    path(
        'tokens/<str:account_token_id>/',
        AccountTokenRetrieveApi.as_view(),
        name='account-token-retrieve',
    ),
]
