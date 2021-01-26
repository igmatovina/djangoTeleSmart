from django.core.management.base import BaseCommand

# import UserFactory here


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--customers',
            default=20,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
        for _ in range(options['customers']):
            CustomerFactory.create()