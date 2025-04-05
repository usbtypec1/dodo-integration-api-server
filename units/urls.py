from django.urls import path

from units.views import UnitListApi


app_name = 'units'
urlpatterns = [
    path('', UnitListApi.as_view(), name='list')
]
