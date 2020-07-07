import os
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


def create_admin(sender, *args, **kwargs):
    if sender.models['user'].objects.count() == 0:
        u = sender.models['user'].objects.create_superuser(
            username=os.getenv('USERNAME'), email=os.getenv('EMAIL'), password=os.getenv('PASSWORD'))
        u.email_user('username and password',
                     f"USERNAME\t{os.getenv('USERNAME')}\nPASSWORD\t{os.getenv('PASSWORD')}\nHappy Coodding!!!")
        print("Y")
    else:
        pass


@receiver(user_logged_in)
def user_is_login(request, user, **kwargs):
	print('*'*12, "login", '*'*12)
	print(f"request: {request}\nuser: {user}\nkwargs: {kwargs}")

@receiver(user_logged_out)
def user_is_logout(request, user, **kwargs):
	print('*'*12, "logout", '*'*12)
	print(f"request: {request}\nuser: {user}\nkwargs: {kwargs}")

@receiver(user_login_failed)
def user_is_outof(credentials, request, **kwargs):
	print('*'*12, "auth", '*'*12)
	print(f"request: {request}\ncredentials: {credentials}\nkwargs: {kwargs}")