from django.forms import ModelForm
from django import forms
from tendik.models import Tendik

class FormTendik(ModelForm):
    class Meta:
        model = Tendik
        fields = ['nip', 'nama', 'jabatan']

        widgets = {
            'nip' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'jabatan' : forms.TextInput({'class':'form-control'}),
        }