from rest_framework.routers import DefaultRouter
from modul_bank.views import BankViewSet

router = DefaultRouter()
router.register(r'banks', BankViewSet, basename='bank')


urlpatterns = router.urls
