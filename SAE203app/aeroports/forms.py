from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class aeroportsForm(ModelForm):
    class Meta :
        model = models.aeroports
        fields = ('nom', 'pays')
        labels = {
            'nom' : _('Nom'),
            'pays' : _('Pays'),
        }