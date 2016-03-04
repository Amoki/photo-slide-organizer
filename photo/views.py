from django.shortcuts import render
from photo.models import MotCle, Groupe
from photo.forms import MotCleForm, DiapoForm, BoiteForm, GroupeForm


def handle_mots(request):
    mot_form = MotCleForm(request.POST)
    if mot_form.is_valid():
        mot_form.save()
    else:
        existing_word = MotCle.objects.get(mot=request.POST.get('mot'))
        copied_request = request.POST.copy()
        for group in existing_word.groupe.all():
            if group.pk not in copied_request.getlist('groupe'):
                copied_request.update({'groupe': group.pk})
        mot_form = MotCleForm(copied_request, instance=existing_word)
        mot_form.save()
    return mot_form


def handle_groupe(request):
    groupe_form = GroupeForm(request.POST)
    if groupe_form.is_valid():
        groupe_form.save()
    return groupe_form


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
    mot_form = MotCleForm()
    diapo_form = DiapoForm()
    boite_form = BoiteForm()
    groupe_form = GroupeForm()

    if request.method == 'POST':
        if request.path == '/mot/':
            mot_form = handle_mots(request)
        elif request.path == '/diapo/':
            diapo_form = handle_diapo(request)
        elif request.path == '/boite/':
            boite_form = handle_boite(request)
        elif request.path == '/groupe/':
            groupe_form = handle_groupe(request)

    groupes = Groupe.objects.all()
    mots_cles = {}
    for groupe in groupes:
        mots_cles[groupe.nom] = MotCle.objects.filter(groupe=groupe)

    data = {
        'mots_cles': mots_cles,
        'groupes': groupes,
        'mot_form': mot_form,
        'diapo_form': diapo_form,
        'boite_form': boite_form,
        'groupe_form': groupe_form,
    }
    return render(request, 'index.html', data)


def search(request):
    results = set()
    if request.method == 'POST':
        tags = request.POST.getlist('description')
        for tag in tags:
            for diapo in MotCle.objects.get(id=tag).diapo_set.all():
                results.add(diapo)

    groupes = Groupe.objects.all()
    mots_cles = {}
    for groupe in groupes:
        mots_cles[groupe.nom] = MotCle.objects.filter(groupe=groupe)

    data = {
        'results': results,
        'mots_cles': mots_cles,
        'groupes': groupes,
    }
    return render(request, 'search.html', data)
