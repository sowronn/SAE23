from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class typeavionsForm(ModelForm):
    class Meta:
        model = models.typeavions
        fields = ('marque', 'description', 'modele', 'longueur_piste', 'image')
        labels = {
            'nom': _('Nom'),
            'descripton': _('description'),
            'modele': _('modele'),
            'longueur_piste': _('longueur_piste'),
            'image': _('image'),
        }
