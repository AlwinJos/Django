from django import forms
from TeachApp.models import Cobra, signup, Image


class code(forms.ModelForm):
    class Meta:
        model = Cobra
        fields = "__all__"
    # friend=forms.CharField(max_length=30)


class Register(forms.ModelForm):
    class Meta:
        model = signup
        fields = '__all__'


class login(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class fpass(forms.Form):
    New_password = forms.CharField()
    Confirm_password = forms.CharField()
    Code =forms.CharField()


class photo(forms.ModelForm):
    class Meta:
        model = Image
        fields='__all__'
