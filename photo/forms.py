from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm
from photo.models import MotCle, Diapo, Boite, Groupe


class MotCleForm(ModelForm):
    class Meta:
        model = MotCle
        fields = ['mot', 'groupe']

    def __init__(self, *args, **kwargs):
        super(MotCleForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class GroupeForm(ModelForm):
    class Meta:
        model = Groupe
        fields = ['nom']

    def __init__(self, *args, **kwargs):
        super(GroupeForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class BoiteForm(ModelForm):
    class Meta:
        model = Boite
        fields = ['repere']

    def __init__(self, *args, **kwargs):
        super(BoiteForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DiapoForm(ModelForm):
    class Meta:
        model = Diapo
        fields = ['boite', 'index', 'description']
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Il y a déjà une diapo enregistrée à cet emplacement",
            }
        }

    def __init__(self, *args, **kwargs):
        super(DiapoForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
