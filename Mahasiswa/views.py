from django.shortcuts import render
from Mahasiswa.models import Mahasiswa
from Mahasiswa.forms import FormMahasiswa
from django.contrib import messages
# Create your views here.
def mahasiswa(request):
    context = {
        'Mahasiswa': Mahasiswa.objects.all()
        
    }
    return render(request,"indexmahasiswa.html", context)


    def tambah_mahasiswa(request):
        if request.POST:
            form = FormMahasiswa(request.POST)
            if form.is_valid():
                form.save()
                form = FormMahasiswa()
                pesan = "Data Berhasil Disimpan"

                konteks = {
                'form' : form,
                'pesan': pesan,
            }

            return render (request, 'tambah-mahasiswa.html', konteks)
        else: 
            form = FormMahasiswa()

        konteks = {
        'form': form
    }

    return render(request, 'tambah-mahasiswa.html', konteks)