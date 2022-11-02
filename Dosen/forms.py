from django.forms import ModelForm
from django import forms
from Dosen.models import Dosen

class FormDosen(ModelForm):
    class Meta:
        model = Dosen
        fields = ['nip', 'nama', 'jabatan', 'email', 'foto']

        widgets = {
            'nip' : forms.NumberInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'jabatan' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'foto' : forms.TextInput({'class':'form-control'}),
        }