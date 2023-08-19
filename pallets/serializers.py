from rest_framework import serializers
from .models import *


class PaletteColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaletteColor
        fields = ('color_code', 'is_dominant')

class PaletteSerializer(serializers.ModelSerializer):
    colors = PaletteColorSerializer(many=True)

    class Meta:
        model = Palette
        fields = ('id', 'user', 'name', 'is_public', 'created_date', 'colors')

    # Override create to handle nested PaletteColor objects
    def create(self, validated_data):
        colors_data = validated_data.pop('colors')
        palette = Palette.objects.create(**validated_data)
        for color_data in colors_data:
            PaletteColor.objects.create(palette=palette, **color_data)
        return palette

class PaletteRevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaletteRevision
        fields = ('palette', 'name', 'revision_date')


class FavoritePaletteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoritePalette
        fields = ('user', 'palette')

    # Ensure the current user is set as the favorite creator
    def create(self, validated_data):
        user = self.context['request'].user
        favorite_palette, created = FavoritePalette.objects.get_or_create(
            user=user, palette=validated_data['palette'])
        return favorite_palette
