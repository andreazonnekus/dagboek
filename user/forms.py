from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django.forms import CharField, PasswordInput, Textarea

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username', 'email']

class CustomUserChangeForm(UserChangeForm):
    email=CharField(label = "Email", widget = Textarea, required=True)

    class Meta:
        model=CustomUser
        fields=['email']

class CustomeLoginFrom(AuthenticationForm):
    class Meta:
        model = CustomUser
        password = CharField(label="Password", widget=PasswordInput) 

class CustomeUserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        password = CharField(label="Password", widget=PasswordInput)