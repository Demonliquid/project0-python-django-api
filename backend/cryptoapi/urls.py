from .views import CryptoViewSet
from rest_framework.routers import DefaultRouter

app_name = 'cryptoapi'

router = DefaultRouter()
router.register('', CryptoViewSet, basename='Crypto')
urlpatterns = router.urls