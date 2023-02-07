from django import forms

class Uploadform(forms.Form):
    file = forms.FileField()
    word = forms.CharField()
