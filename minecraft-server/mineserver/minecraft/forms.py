from django import forms


class PlayerForm(forms.Form):
    name = forms.CharField()


class UserForm(forms.Form):
    name = forms.CharField(label='Your username...', max_length=100)
    password = forms.CharField(label='Your password...', max_length=100)