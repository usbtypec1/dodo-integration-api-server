from django.core.management import BaseCommand

from accounts.use_cases import AccountTokensUpdateUseCase


class Command(BaseCommand):

    def handle(self, *args, **options):
        AccountTokensUpdateUseCase().execute()
        self.stdout.write(
            self.style.SUCCESS("Successfully refreshed API tokens.")
        )
