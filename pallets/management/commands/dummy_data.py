import random
from django.core.management.base import BaseCommand
from pallets.models import User, Palette, PaletteColor

class Command(BaseCommand):
    help = 'Add dummy data for palettes'

    # Generates a random hex color
    def random_color(self):
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

    def handle(self, *args, **kwargs):
        # Let's assume you have a user in the database to associate these palettes with.
        # You can modify this as per your setup.
        user = User.objects.first()

        if not user:
            self.stdout.write(self.style.ERROR('No user found in database. Please create a user first.'))
            return

        for _ in range(20):
            palette = Palette.objects.create(
                user=user,
                name=f'Dummy Palette {_}',
                is_public=random.choice([True, False])
            )

            # 1 to 2 dominant colors
            for _ in range(random.randint(1, 2)):
                PaletteColor.objects.create(
                    palette=palette,
                    color_code=self.random_color(),
                    is_dominant=True
                )

            # 2 to 4 accent colors
            for _ in range(random.randint(2, 4)):
                PaletteColor.objects.create(
                    palette=palette,
                    color_code=self.random_color(),
                    is_dominant=False
                )

        self.stdout.write(self.style.SUCCESS('Successfully added dummy palettes'))
