from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Palette, PaletteColor, FavoritePalette, PaletteRevision
from .serializers import PaletteSerializer, PaletteColorSerializer, FavoritePaletteSerializer, PaletteRevisionSerializer
from rest_framework.permissions import AllowAny

class PaletteViewSet(viewsets.ModelViewSet):
    queryset = Palette.objects.all()
    serializer_class = PaletteSerializer

    def get_permissions(self):
        # If the user is trying to list palettes and they're not authenticated, we'll show them only public palettes
        if self.action == 'list' and not self.request.user.is_authenticated:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(PaletteViewSet, self).get_permissions()

    def get_queryset(self):
        # If the user is authenticated, show them all their palettes
        if self.request.user.is_authenticated:
            return Palette.objects.filter(user=self.request.user)
        # If the user is not authenticated, show them only public palettes
        else:
            return Palette.objects.filter(is_public=True)

    def perform_create(self, serializer):
        # Assign the current user to the palette being created
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # Save the current state to PaletteRevision before updating
        palette = self.get_object()
        PaletteRevision.objects.create(palette=palette, name=palette.name)
        serializer.save()

class PaletteColorViewSet(viewsets.ModelViewSet):
    queryset = PaletteColor.objects.all()
    serializer_class = PaletteColorSerializer
    permission_classes = [IsAuthenticated]

class FavoritePaletteViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin):
    queryset = FavoritePalette.objects.all()
    serializer_class = FavoritePaletteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only show favorites of the logged-in user
        return FavoritePalette.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def add_to_favorites(self, request, pk=None):
        palette = get_object_or_404(Palette, pk=pk)
        favorite, created = FavoritePalette.objects.get_or_create(user=request.user, palette=palette)
        if created:
            return Response({'status': 'palette added to favorites'}, status=status.HTTP_201_CREATED)
        return Response({'status': 'palette already in favorites'}, status=status.HTTP_400_BAD_REQUEST)

class PaletteRevisionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PaletteRevision.objects.all()
    serializer_class = PaletteRevisionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        palette_id = self.request.query_params.get('palette_id', None)
        if palette_id:
            return PaletteRevision.objects.filter(palette=palette_id)
        return super().get_queryset()
