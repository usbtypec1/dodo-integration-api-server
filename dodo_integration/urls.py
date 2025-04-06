from django.conf import settings
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(f'{settings.ROOT_PATH}admin/', admin.site.urls),
    path(
        f'{settings.ROOT_PATH}v1/telegram/',
        include('telegram.urls'),
    ),
    path(
        f'{settings.ROOT_PATH}v1/reports/',
        include('reports.urls'),
    ),
    path(
        f'{settings.ROOT_PATH}v1/accounts/',
        include('accounts.urls'),
    ),
    path(
        f'{settings.ROOT_PATH}v1/units/',
        include('units.urls'),
    ),
]
