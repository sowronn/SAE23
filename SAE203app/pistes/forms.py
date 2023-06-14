from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class pistesForm(ModelForm):
    class Meta:
        model = models.pistes
        fields = ('numero', 'longueur', 'aeroport')
        labels = {
            'numero': _('Numero'),
            'longueur': _('Longueur'),
            'aeroport': _('Aeroport'),
        }
