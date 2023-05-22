from django.db import models
from user.models import Profile



class Cancer(models.Model):
    age = models.IntegerField()
    num_of_sex_partners = models.IntegerField()
    first_intercourse = models.IntegerField() # age
    num_of_pregnancies = models.IntegerField()
    smokes = models.BooleanField()
    smokes_years = models.IntegerField()
    smokes_packs_year = models.IntegerField()
    hormonal_contracpetives = models.BooleanField()
    hormonal_contracpetives_years = models.IntegerField()
    IUD = models.BooleanField()
    IUD_years = models.IntegerField()
    STDs = models.BooleanField()
    STDs_number = models.IntegerField()
    STD_condylomatosis = models.BooleanField()
    STD_cervical_codylomatosis = models.BooleanField()
    STD_vaginal_condylomatosis = models.BooleanField()
    STD_vulvo_perineal_codylomatosis = models.BooleanField()
    STD_syphilis = models.BooleanField()
    STD_pelvic_inflammatory_disease = models.BooleanField()
    STD_genital_herpes = models.BooleanField()
    STD_molluscum_contagiosum = models.BooleanField()
    STD_AIDS = models.BooleanField()
    STD_HIV = models.BooleanField()
    STD_Hepatitis_B = models.BooleanField()
    STD_HPV = models.BooleanField()
    STD_num_of_diagnosis = models.IntegerField()
    Dx_cancer = models.BooleanField()
    Dx_CIN = models.BooleanField()
    Dx_HPV = models.BooleanField()
    Dx = models.BooleanField()
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    # target
    Hinselmann = models.BooleanField(null=True, blank=True)
    Schiller = models.BooleanField(null=True, blank=True)
    Cytology = models.BooleanField(null=True, blank=True)
    Biopsy = models.BooleanField(null=True, blank=True)

    class Meta:
        verbose_name = 'Рак шейки матки'
        verbose_name_plural = 'Раковые заболевания'
# Create your models here.
