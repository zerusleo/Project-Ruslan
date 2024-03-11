from django import forms

from proj.models import Img


class ImageForm(forms.ModelForm):
    class Meta:
        model = Img
        fields = ('Image', 'title')
#внутри созданного forms.py создаем форму