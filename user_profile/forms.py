from django.contrib.auth.models  import User
from django.contrib.auth.forms  import UserCreationForm,UserChangeForm

class register_user(UserCreationForm):
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
        ]

class update_form(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
        ]