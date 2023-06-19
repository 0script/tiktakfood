from .views import ProductView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product-list', ProductView, basename='product')
urlpatterns = router.urls