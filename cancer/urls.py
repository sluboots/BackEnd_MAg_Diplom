from django.urls import path
from .views import cancer_view
from heart_disease.views import HeartCreateView

urlpatterns = [
    path('', cancer_view),
    path('add/', HeartCreateView.as_view(), name='add')
]