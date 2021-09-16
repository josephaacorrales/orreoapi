from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.viewsets import UserGw2KeysViewSet

router = DefaultRouter()
router.register(r'gw2keys', UserGw2KeysViewSet, basename="gw2key")

urlpatterns = [
    # Including admin site during initial debugging
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]