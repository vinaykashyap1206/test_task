import json
import os

from django.core.management.base import BaseCommand, CommandError

from blogs.models import Blog

from . import data

class Command(BaseCommand):
    help = 'Populate Blog data'

    def handle(self, *args, **options):
        self.add_blogs()
        self.stdout.write(self.style.SUCCESS('Successfully triggered'))

    def add_blogs(self):
        for dt in data.DATA:
            blog = Blog.objects.create(**dt)
            print('new blog object created')