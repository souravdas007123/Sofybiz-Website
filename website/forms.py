from django import forms

class Queryform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    number=forms.CharField()
    address=forms.CharField()
    queries=forms.CharField()