import os

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError

from images.models import Image

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('directory')

    def handle(self, *args, **options):
        for i in os.listdir(options['directory']):
            im = Image()
            path = options['directory'] + os.sep + i
            with open(path) as f:
              data = f.read()

            # obj.image is the ImageField
            im.image = i
            im.image.save(i, ContentFile(data))
            im.save()