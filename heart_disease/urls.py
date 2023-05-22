from django.urls import path
from .views import heart_view, by_heart_disease, HeartCreateView

urlpatterns = [
    path('', heart_view, name='index'),
    path('<int:heart_disease_id>/', by_heart_disease, name='heart_disease'),
    path('add/', HeartCreateView.as_view(), name='add')
]