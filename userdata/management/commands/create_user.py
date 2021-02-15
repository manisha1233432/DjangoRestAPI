
from django.core.management.base import BaseCommand
from userdata.models import Usermodel



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('id')
        parser.add_argument('real_name')
        parser.add_argument('tz')

    def handle(self, *args, **options):
        user = Usermodel(
            id = options['id'],
            real_name = options['real_name'],
            tz = options['tz']
        )
        user.save()
        self.stdout.write(self.style.SUCCESS('Added user'))
        


        