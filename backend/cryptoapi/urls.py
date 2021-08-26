from .views import CryptoViewSet, DolarViewSet
from rest_framework.routers import SimpleRouter

app_name = 'cryptoapi'

router = SimpleRouter()
router.register('crypto', CryptoViewSet, basename ='cryptos')
router.register('dollar', DolarViewSet, basename ='dollars')
urlpatterns = router.urls

