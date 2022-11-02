from django.shortcuts import render
from tendik.models import Tendik
from tendik.forms import FormTendik
from django.contrib import messages
# Create your views here.
def tendik(request):
    context = {
        'tendik': Tendik.objects.all()
        
    }
    return render(request,"indextendik.html", context)

def tambah_tendik(request):
    if request.POST:
        form = FormTendik(request.POST)
        if form.is_valid():
            form.save()
            form = FormTendik()
            pesan = "Data Berhasil Disimpan"

            konteks = {
                'form' : form,
                'pesan': pesan,
            }

            return render (request, 'tambah-tendik.html', konteks)
    else: 
        form = FormTendik()

    konteks = {
        'form': form
    }

    return render(request, 'tambah-tendik.html', konteks)