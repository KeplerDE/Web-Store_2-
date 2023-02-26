from django.contrib.auth.forms import AuthenticationForm
from users.models import User                # связываем форму с нашей моделью


#https://github.com/django/django/blob/2276ec8c21655b05bb44e14e236b499aa5d01f5b/django/contrib/auth/forms.py#L18
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

