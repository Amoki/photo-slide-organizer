from django.shortcuts import render
from django.db.models import Q
from photo.models import MotCle, Diapo
from photo.forms import DiapoForm, BoiteForm


def handle_boite(request):
    boite_form = BoiteForm(request.POST)
    if boite_form.is_valid():
        boite_form.save()
    return boite_form


def handle_diapo(request):
    diapo_form = DiapoForm(request.POST)
    if diapo_form.is_valid():
        diapo_form.save()
    return diapo_form


def home(request):
    diapo_form = DiapoForm()
    boite_form = BoiteForm()

    if request.method == 'POST':
        if request.path == '/diapo/':
            diapo_form = handle_diapo(request)
        elif request.path == '/boite/':
            boite_form = handle_boite(request)

    data = {
        'diapo_form': diapo_form,
        'boite_form': boite_form,
    }
    return render(request, 'index.html', data)


def search(request):
    results = []
    if request.method == 'POST':
        tags = request.POST.getlist('description')
        print(tags)
        diapos = Diapo.objects.all()
        for tag in tags:
            diapos = diapos.filter(words__pk=tag)
        results = list(diapos)

    data = {
        'results': results,
        'mots_cles': MotCle.objects.all().order_by('mot')
    }
    return render(request, 'search.html', data)
