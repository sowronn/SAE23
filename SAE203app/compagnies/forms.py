from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class compagniesForm(ModelForm):
    class Meta:
        model = models.compagnies
        fields = ('nom', 'description', 'paysderatachement')
        labels = {
            'nom': _('Nom'),
            'description': _('description'),
            'paysderatachement': _('paysderatachement'),
        }
