from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class avionsForm(ModelForm):
    class Meta:
        model = models.avions
        fields = ('nom', 'compagnie', 'modele')
        labels = {
            'nom': _('Nom'),
            'compagnie': _('compagnie'),
            'modele': _('modele'),
        }
