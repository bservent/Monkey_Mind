from django.forms import ModelForm
from .models import Profile

class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'login', 'imageURL']