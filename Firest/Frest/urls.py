from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PaketViewSet, LanggananViewSet, register_user

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pakets', PaketViewSet)
router.register(r'langganans', LanggananViewSet)

urlpatterns = [
    path('users/register/', register_user, name='register-user'),  # ✅ Endpoint untuk registrasi
    path('', include(router.urls)),  # ✅ Endpoint lainnya
]
