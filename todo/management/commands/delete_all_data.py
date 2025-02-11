from django.core.management.base import BaseCommand
from todo.models import Task, TaskDate

class Command(BaseCommand):
    help = 'Delete all data from Task and TaskDate models'

    def handle(self, *args, **kwargs):
        TaskDate.objects.all().delete()
        Task.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all data from Task and TaskDate models'))