from django.urls import path, re_path
from core.views import GatewayView

app_name = "core"
urlpatterns = [re_path(r'.*', GatewayView.as_view(), name="main")]
