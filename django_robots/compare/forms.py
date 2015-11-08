from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your forms here.

class UploadImage(forms.Form):
    image_desc = forms.CharField(max_length=255)
    image_file = forms.ImageField()

class VoteForm(forms.Form):
    winner = forms.IntegerField(widget=forms.HiddenInput)
    loser = forms.IntegerField(widget=forms.HiddenInput)
    placement = forms.CharField(widget=forms.HiddenInput)

class SignUpForm(forms.Form):
    fname = forms.CharField()
    lname = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def username_is_valid(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return True
        return False

    def email_is_valid(self):
        try:
            email = User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return True
        return False

    def passwords_match(self):
        return self.cleaned_data['password'] == self.cleaned_data['confirm_password']

    def passwords_meet_requirements(self):
        return len(self.cleaned_data['password']) >= 8

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def auth(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                return 2 # Active User
            else:
                return 1 # Inactive User
        else:
            return 0 # Bad login
