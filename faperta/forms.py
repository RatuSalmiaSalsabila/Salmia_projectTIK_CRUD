from django.forms import Modelform
from faperta.models import Prodi

class FormProdi(ModelForm):
    class Meta:
        Model = Prodi
        fields = '__all__'