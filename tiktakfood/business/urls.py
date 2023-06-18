# from django.urls import path, include
# from .views import *

# urlpatterns=[
#     path('latest-business/',BusinessView.as_view()),
# ]

from .views import BusinessView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'business-list', BusinessView, basename='business')
urlpatterns = router.urls