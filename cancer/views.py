from django.shortcuts import render
from cancer.models import Cancer



from django.http import HttpResponse


def cancer_view(request):
    cancers = Cancer.objects.all()
    context = {'cancers': cancers}
    return render(request, 'index_cancer.html', context)
# Create your views here.
