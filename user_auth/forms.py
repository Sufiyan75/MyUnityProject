from django import forms
from .models import Registration

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = Registration
#         fields = [
#             'username',
#             'password'
#         ]
#         widgets = {
#             'password': forms.PasswordInput(),
#         }