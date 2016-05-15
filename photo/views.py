from django.shortcuts import render
from photo.models import MotCle, Diapo
from photo.forms import DiapoForm


def home(request):
    diapo_form = DiapoForm()
    save_success = False
    if request.method == 'POST':
        diapo_form = DiapoForm(request.POST)
        if diapo_form.is_valid():
            diapo_form.save()
            save_success = True

    data = {
        'diapo_form': diapo_form,
        'save_success': save_success and not diapo_form.errors
    }
    return render(request, 'index.html', data)


def search(request):
    results = []
    if request.method == 'POST':
        tags = request.POST.getlist('description')
        diapos = Diapo.objects.all()
        for tag in tags:
            diapos = diapos.filter(words__pk=tag)
        results = list(diapos)

    data = {
        'results': results,
        'mots_cles': MotCle.objects.all().order_by('mot')
    }
    return render(request, 'search.html', data)
