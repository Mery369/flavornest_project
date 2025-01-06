from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

# class EmailAuthBackend(ModelBackend):
#     """
#     Authenticate using the email address instead of the username.
#     """
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(email=username)
#             if user.check_password(password):
#                 return user
#         except User.DoesNotExist:
#             return None
