from django.forms import ModelForm

from .models import Heart

class HeartForm(ModelForm):
    class Meta:
        model = Heart
        fields = ('age', 'sex', 'cp', 'trestbps', 'fbs', 'restecg', 'thalach',
                  'exang', 'oldpeak', 'slope', 'ca', 'thal', 'disease_type')
