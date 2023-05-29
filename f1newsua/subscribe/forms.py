from .models import Followers
from django.forms import ModelForm, EmailInput

class FollowersForm(ModelForm):
    class Meta:
        model = Followers
        fields = ['email']

        widgets = {
            'email': EmailInput(attrs={
                'class': "block__email",
                'placeholder': "email"
            })
        }