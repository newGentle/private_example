from django import forms
from .models import upload_file

class Uploadform(forms.ModelForm):
    file = forms.FileField(label='')
    word = forms.CharField(label='Искомое слово')
    class Meta:
        model = upload_file
        fields = ['file', 'word']
        
