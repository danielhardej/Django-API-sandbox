from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Send an invite email to a new admin user'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username of the new admin user')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        try:
            user = User.objects.get(username=username)
            send_mail(
                'Admin Account Created',
                f'Hello {user.username},\n\nYour admin account has been created. You can log in with your email: {user.email}\n\nBest regards,\nYour Team',
                'your-email@example.com',
                [user.email],
                fail_silently=False,
            )
            self.stdout.write(self.style.SUCCESS(f'Invite email sent to {user.email}'))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'User with username {username} does not exist'))