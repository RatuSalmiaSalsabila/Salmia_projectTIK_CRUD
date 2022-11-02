from django.forms import ModelForm
from django import forms
from Mahasiswa.models import Mahasiswa


class FormMahasiswa(ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ['nama', 'nim', 'ttl', 'email', 'foto']

        widgets = {
            'nama' : forms.NumberInput({'class':'form-control'}),
            'nim' : forms.TextInput({'class':'form-control'}),
            'ttl' : forms.TextInput({'class':'form-control'}),
            'email' : forms.TextInput({'class':'form-control'}),
            'foto' : forms.TextInput({'class':'form-control'}),
        }