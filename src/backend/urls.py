from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.permissions import AllowAny

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from subway.views import get_status, get_uptime

router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/subway/status/", get_status, name="subway-status"),
    path("api/subway/uptime/", get_uptime, name="subway-uptime"),
    path("", include(router.urls)),
]

# # Django debug toolbar
# import debug_toolbar
# urlpatterns += [
#     path('__debug__/', include(debug_toolbar.urls)),
# ]
