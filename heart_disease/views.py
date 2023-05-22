from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Heart, Type_Heart_Disease
from .forms import HeartForm

#Вывод всех записей
def heart_view(request):
    hearts = Heart.objects.all()
    type_heart = Type_Heart_Disease.objects.all()
    context = {'hearts': hearts, 'type_heart': type_heart}
    return render(request, 'index.html', context)

#Вывод записей по конкретным болезням
def by_heart_disease(request, heart_disease_id):
    hearts = Heart.objects.filter(disease_type=heart_disease_id)
    type_disease = Type_Heart_Disease.objects.all()
    current_type_disease = Type_Heart_Disease.objects.get(pk=heart_disease_id)
    context = {'hearts': hearts, 'type_disease': type_disease, 'current_type_disease': current_type_disease}
    return render(request, 'heart_disease_type.html', context)


class HeartCreateView(CreateView):
    template_name = 'create.html'
    form_class = HeartForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disease_type'] = Type_Heart_Disease.objects.all()
        return context
# Create your views here.
