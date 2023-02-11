from django.shortcuts import render, redirect
from .models import *
from .forms import *

def bosh_sahifa(request):
    return render(request, 'bosh_sahifa.html')

def hamma_mualliflar(request):
    qidiruv_soz = request.GET.get("qidirish")
    if request.method == 'POST':
        form = MuallifForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/mualliflar/')
    if qidiruv_soz:
        data = {
            "mualliflar": Muallif.objects.filter(ism__contains=qidiruv_soz)
        }
        return render(request, "hamma_mualliflar.html", data)
    data = {
        'forma': MuallifForm(),
        "mualliflar": Muallif.objects.all()
    }
    return render(request, "hamma_mualliflar.html", data)

def hamma_kitoblar(request):
    qidiruv_soz = request.GET.get('qidirish')
    if request.method == 'POST':
        form = KitobForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/kitoblar/')
    if qidiruv_soz:
        data = {
            'kitoblar': Kitob.objects.filter(nom__contains=qidiruv_soz)
        }
        return render(request, 'hamma_kitoblar.html', data)
    data = {
        'form': KitobForm(),
        'kitoblar': Kitob.objects.all()
    }
    return render(request, 'hamma_kitoblar.html', data)

def hamma_recordlar(request):
    qidruv_soz = request.GET.get("qidirish")
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/recordlar/')
    if qidruv_soz:
        data = {
            "recordlar": Record.objects.filter(talaba__ism__contains=qidruv_soz)
        }
        return render(request, 'hamma_recordlar.html', data)

    data = {
        "recordlar": Record.objects.all(),
        'form': RecordForm()
    }
    return render(request, "hamma_recordlar.html", data)

def hamma_adminlar(request):
    qidiruv_soz = request.GET.get('qidirish')
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/adminlar/')
    if qidiruv_soz:
        data = {
            'adminlar': Admin.objects.filter(ism__contains=qidiruv_soz)
        }
        return render(request, 'hamma_adminlar.html', data)
    data = {
        'adminlar': Admin.objects.all(),
        'forma': AdminForm()
    }
    return render(request, 'hamma_adminlar.html', data)

def hamma_talabalar(request):
    qidiruv_soz = request.GET.get('qidirish')
    if request.method == "POST":
        forma = TalabaForm(request.POST)
        if forma.is_valid():
            Talaba.objects.create(
                ism=forma.cleaned_data.get('name'),
                kitob_soni=forma.cleaned_data.get('nums_of_books'),
                kurs=forma.cleaned_data.get('course'),
                bitruvchi=forma.cleaned_data.get('senior')
            )
        return redirect('/talabalar/')
    if qidiruv_soz:
        data = {
            'talabalar': Talaba.objects.filter(ism__contains=qidiruv_soz)
        }
        return render(request, "hamma_talabalar.html", data)
    data = {
        'talabalar': Talaba.objects.all(),
        'forma': TalabaForm()
    }
    return render(request, "hamma_talabalar.html", data)

def bitta_muallif(request, son):
    if request.method == 'POST':
        if request.POST.get('t') == 'on':
            qiymat = True
        else:
            qiymat = False
        Muallif.objects.filter(id=son).update(
            ism=request.POST.get('i'),
            tugilgan_yil=request.POST.get('t_y'),
            trik=qiymat,
            kitob_soni=request.POST.get('k_s'),
            jinsi=request.POST.get('j')
        )
        return redirect('/mualliflar/')
    data = {
        'muallif': Muallif.objects.get(id=son)
    }
    return render(request, 'tanlangan_muallif.html', data)


def bitta_kitob(request, son):
    if request.method == 'POST':
        Kitob.objects.filter(id=son).update(
            nom=request.POST.get('n'),
            sahifa=request.POST.get('s'),
            janr=request.POST.get('j'),
            muallif=Muallif.objects.get(id=request.POST.get('m'))
        )
        return redirect('/kitoblar/')
    data = {
        'kitob': Kitob.objects.get(id=son),
        'mualliflar': Muallif.objects.all()
    }
    return render(request, 'tanlangan_kitob.html', data)

def bitta_record(request, son):
    if request.method == 'POST':
        if request.POST.get('q') == 'on':
            qiymat = True
        else:
            qiymat = False
        Record.objects.filter(id=son).update(
            qaytardi=qiymat,
            qaytargan_sana=request.POST.get('q_s')
        )
        return redirect('/recordlar/')
    data = {
        'record': Record.objects.get(id=son)
    }
    return render(request, 'tanlangan_recordlar.html', data)

def bitta_admin(request, son):
    if request.method == 'POST':
        Admin.objects.filter(id=son).update(
            ism=request.POST.get('i'),
            ish_vaqti=request.POST.get('v')
        )
        return redirect("/adminlar/")
    data = {
        'admin': Admin.objects.get(id=son)
    }
    return render(request, 'tanlangan_admin.html', data)

def bitta_talaba(request, son):
    if request.method == 'POST':
        if request.POST.get('b') == 'on':
            qiymat = True
        else:
            qiymat = False
        Talaba.objects.filter(id=son).update(
            ism=request.POST.get('i'),
            kurs=request.POST.get('k'),
            kitob_soni=request.POST.get('k_s'),
            bitruvchi=qiymat
        )
        return redirect(f"/talaba/{son}/")

    data = {
        'talaba': Talaba.objects.get(id=son)
    }
    return render(request, 'tanlangan_talabalar.html', data)





def muallif_ochrish(request, son):
    muallif = Muallif.objects.get(id=son)
    muallif.delete()

    return redirect("/mualliflar/")

def kitob_ochirish(request, son):
    kitob = Kitob.objects.get(id=son)
    kitob.delete()

    return redirect("/kitoblar/")

def record_ochrish(request, son):
    record = Record.objects.get(id=son)
    record.delete()

    return redirect("/recordlar/")

def talaba_ochrish(request, son):
    talaba = Talaba.objects.get(id=son)
    talaba.delete()

    return redirect('/talabalar/')

def admin_ochrish(request, son):
    admin = Admin.objects.get(id=son)
    admin.delete()

    return redirect('/adminlar/')



