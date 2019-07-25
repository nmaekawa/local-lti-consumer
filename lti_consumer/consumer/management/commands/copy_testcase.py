
from django.core.management import BaseCommand

from consumer.views import copy_testcase


class Command(BaseCommand):
    help = 'copy testcase and launch params'

    def add_arguments(self, parser):
        parser.add_argument(
            '--name', required=True,
            help='testcase name to be copied'
        )

    def handle(self, *args, **kwargs):
        source_name = kwargs['name']

        target_testcase = copy_testcase(source_name)
        print('created testcase `{}`'.format(target_testcase.name))


