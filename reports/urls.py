from django.urls import path

from reports.views import ReportRouteListCreateDeleteApi


app_name = "reports"
urlpatterns = [
    path(
        r'routes/',
        ReportRouteListCreateDeleteApi.as_view(),
        name='report-route-list-create-delete',
    ),
]
