from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.db.utils import IntegrityError
from django import forms
from django.forms import ModelForm
from photo.models import Diapo, Localisation


class DiapoForm(ModelForm):
    # add fields used by Localisations
    localisation_type = forms.ChoiceField(choices=Localisation.TYPE_LOCALISATION, label='Type de localisation')
    localisation_num = forms.CharField(max_length=128, label='Label de la localisation')

    class Meta:
        model = Diapo
        fields = ['index', 'description']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Il y a déjà une diapo enregistrée à cet emplacement",
            }
        }

    def __init__(self, *args, **kwargs):
        super(DiapoForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        instance = super(DiapoForm, self).save(commit=False)

        localisation, created = Localisation.objects.get_or_create(
            numero=self.cleaned_data['localisation_num'],
            type=self.cleaned_data['localisation_type']
        )

        instance.localisation_id = localisation.pk
        if commit:
            try:
                instance.save()
            except IntegrityError:
                self.add_error(None, ValidationError('Une photo existe déjà à cet emplacement', code='invalid'))
            except:
                self.add_error(None, ValidationError('Une erreur inconnue est survenue, les champs sont-ils correctement saisis ?', code='error'))
        return instance
