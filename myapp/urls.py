from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import RedirectView
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', RedirectView.as_view(url='/items/', permanent=True)),  # Redirect root URL to /items
    path('', include(router.urls)),
]