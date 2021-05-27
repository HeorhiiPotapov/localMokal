from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, Profile, Phone


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'password1', 'password2')


class CustomUserEditForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'email')


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('logo', 'brand', 'city', 'address')


class AddPhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        exclude = ('profile', )
