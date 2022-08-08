from django import forms

from .models import apply , job


class applyform(forms.ModelForm):
    class Meta:
        model = apply
        fields = ['name','email' , 'cv' ,'website']


class jobform(forms.ModelForm):
    class Meta:
        model = job
        fields = "__all__"
        exclude = ('slug','owner',)

