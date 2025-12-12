from django import forms
class UserRegistrationForm(forms.Form):
    GENDER_OPTIONS = ["MALE", "FEMALE"]
    firstName = forms.CharField(required=False)
    lastName = forms.CharField()
    email = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER_OPTIONS))