from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaletteViewSet, PaletteColorViewSet, FavoritePaletteViewSet, PaletteRevisionViewSet

router = DefaultRouter()
router.register(r'palettes', PaletteViewSet)
router.register(r'palette-colors', PaletteColorViewSet)
router.register(r'favorites', FavoritePaletteViewSet)
router.register(r'palette-revisions', PaletteRevisionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
