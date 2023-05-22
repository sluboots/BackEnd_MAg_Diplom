from django.db import models
from user.models import Profile



class Heart(models.Model):
    age = models.IntegerField()
    sex = models.BooleanField()
    cp = models.IntegerField() # chest pain type. 1: typical angina,  2: atypical angina, 3: non-anginal pain, 4: asymptomatic
    trestbps = models.IntegerField() #  resting blood pressure (in mm Hg on admission to the hospital)
    chol = models.IntegerField(null = True)
    fbs = models.BooleanField() # (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
    restecg = models.IntegerField() # resting electrocardiographic results, 0: normal, 1:  having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
    thalach = models.IntegerField() # maximumheart rate achieved
    exang = models.BooleanField() # exercise induced angina (1 = yes; 0 = no)
    oldpeak = models.FloatField() #  ST depression induced by exercise relative to rest
    slope = models.IntegerField() # the slope of the peak exercise ST segment, 1: upsloping, 2: flat, 3: downsloping
    ca = models.IntegerField() # number of major vessels (0-3) colored by flourosopy
    thal = models.IntegerField() # 3 = normal, 6 = fixed defect, 7 = reversable defect
    disease_type = models.ForeignKey('Type_Heart_Disease', null=True, on_delete=models.PROTECT, verbose_name='Название болезни')
    target = models.BooleanField(null = True, blank=True) # 0: < 50% diameter narrowing. 1: > 50% diameter narrowing
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Заболевание сердца'
        verbose_name_plural = 'Заболевания сердца'
# Create your models here.


class Type_Heart_Disease(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Название болезни сердца')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Название болезней'
        verbose_name = 'Болезнь'
        ordering = ['name']