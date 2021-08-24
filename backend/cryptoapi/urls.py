from .views import CryptoViewSet, DolarViewSet
from rest_framework.routers import DefaultRouter

app_name = 'cryptoapi'

router = DefaultRouter()
router.register('', CryptoViewSet, basename='Crypto')
urlpatterns = router.urls

router = DefaultRouter()
router.register('', DolarViewSet, basename='Crypto')
urlpatterns = router.urls