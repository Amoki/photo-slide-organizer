from django.core.exceptions import NON_FIELD_ERRORS
from django import forms
from django.forms import ModelForm
from photo.models import MotCle, Diapo


class MotCleForm(ModelForm):
    class Meta:
        model = MotCle
        fields = ['mot']

    def __init__(self, *args, **kwargs):
        super(MotCleForm, self).__init__(*args, **kwargs)

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
        # self.fields["description"].widget = forms.widgets.CheckboxSelectMultiple()
        # self.fields["description"].help_text = ""
        # self.fields["description"].queryset = MotCle.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
