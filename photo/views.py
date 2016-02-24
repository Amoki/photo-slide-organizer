from django.shortcuts import render
from photo.models import MotCle, Diapo
from photo.forms import MotCleForm, DiapoForm


def handle_mots(request):
    mot_form = MotCleForm(request.POST)
    if mot_form.is_valid():
        mot_form.save()
    return mot_form


def handle_diapo(request):
    diapo_form = DiapoForm(request.POST)
    if diapo_form.is_valid():
        diapo_form.save()
    return diapo_form


def home(request):
    mots_cles = MotCle.objects.all()
    mot_form = MotCleForm()
    diapo_form = DiapoForm()

    print(request.POST)
    if request.method == 'POST':
        if request.POST.get('mot', False):
            mot_form = handle_mots(request)
        elif request.POST.get('boite', False):
            diapo_form = handle_diapo(request)

    # GET
    data = {
        'mots_cles': mots_cles,
        'mot_form': mot_form,
        'diapo_form': diapo_form
    }
    return render(request, 'index.html', data)
