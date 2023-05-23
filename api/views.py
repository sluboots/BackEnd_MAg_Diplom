import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework import generics
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from .serializers import BloodCellListSerializer

from blood_cell.models import Blood_Cell
from heart_disease.models import Heart
from cancer.models import Cancer
from api.serializers import HeartDiseaseListSerializer, CancerListSerializer, RegisterSerializer
from heart_disease.functions import classification_heart_disease
from cancer.functions import classification_cancer
from django.contrib.auth.models import AnonymousUser

@api_view(['GET', 'POST'])
def getRoutes(request):
    routes = [
        {'GET': 'api/view_heart'},
        {'GET': 'api/heart/id'},
        {'GET': 'api/view_cancer'},
        {'GET': 'api/cancer/id'},

        {'POST': 'api/add_heart'},
        {'POST': 'api/add_cancer'},
    ]

    return Response(routes)


@api_view(['POST'])
@permission_classes([AllowAny])
def addHeart(request):
    profile = None
    if isinstance(request.user, AnonymousUser):
        profile = None
    else:
        profile = request.user.profile
    data_post = request.data
    data = data_post.get('post')
    res = classification_heart_disease(data)
    new_heart = Heart.objects.create(age=data.get('age'), sex=data.get('sex'), cp=data.get('cp'),
                                     trestbps=data.get('trestbps'), fbs=data.get('fbs'), restecg=data.get('restecg'),
                                     thalach=data.get('thalach'), exang=data.get('exang'), oldpeak=data.get('oldpeak'),
                                     slope=data.get('slope'), ca=data.get('ca'), thal=data.get('thal'), chol=data.get('chol'),
                                     target = res, owner = profile)
    new_heart.save()
    serializer = HeartDiseaseListSerializer(new_heart)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([AllowAny])
def addCancer(request):
    profile = None
    if isinstance(request.user, AnonymousUser):
        profile = None
    else:
        profile = request.user.profile
    data_post = request.data
    data = data_post.get('post')
    Schiller, Hinselmann, Cytology, Biopsy = classification_cancer(data)
    new_cancer = Cancer.objects.create(age=data.get('age'), num_of_sex_partners=data.get('num_of_sex_partners'),
                                       first_intercourse=data.get('first_intercourse'), num_of_pregnancies=data.get('num_of_pregnancies'),
                                       smokes=data.get('smokes'), smokes_years=data.get('smokes_years'), smokes_packs_year=data.get('smokes_packs_year'),
                                       hormonal_contracpetives=data.get('hormonal_contracpetives'), hormonal_contracpetives_years=data.get('hormonal_contracpetives_years'),
                                       IUD=data.get('IUD'), IUD_years=data.get('IUD_years'), STDs=data.get('STDs'), STDs_number=data.get('STDs_number'),
                                       STD_condylomatosis=data.get('STD_condylomatosis'), STD_cervical_codylomatosis=data.get('STD_cervical_codylomatosis'),
                                       STD_vaginal_condylomatosis=data.get('STD_vaginal_condylomatosis'), STD_vulvo_perineal_codylomatosis=data.get('STD_vulvo_perineal_codylomatosis'),
                                       STD_syphilis=data.get('STD_syphilis'), STD_pelvic_inflammatory_disease=data.get('STD_pelvic_inflammatory_disease'),
                                       STD_genital_herpes=data.get('STD_genital_herpes'), STD_molluscum_contagiosum=data.get('STD_molluscum_contagiosum'), STD_AIDS=data.get('STD_AIDS'), STD_HIV=data.get('STD_HIV'),
                                       STD_Hepatitis_B=data.get('STD_Hepatitis_B'), STD_HPV=data.get('STD_HPV'), STD_num_of_diagnosis=data.get('STD_num_of_diagnosis'),
                                       Dx_cancer=data.get('Dx_cancer'), Dx_CIN=data.get('Dx_CIN'), Dx_HPV=data.get('Dx_HPV'), Dx=data.get('Dx'), Hinselmann=Hinselmann, Schiller=Schiller, Cytology=Cytology, Biopsy=Biopsy, owner=profile)
    new_cancer.save()
    serializer = CancerListSerializer(new_cancer)
    return Response(serializer.data)


@api_view(['GET'])
def viewCancer(request):
    profile = request.user.profile
    cancer = profile.cancer_set.all()
    serializer = CancerListSerializer(cancer, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewHeartDisease(request):
    profile = request.user.profile
    heart = profile.heart_set.all()
    serializer = HeartDiseaseListSerializer(heart, many=True)
    return Response(serializer.data)

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    parser_classes = [FormParser, MultiPartParser, JSONParser]

class BloodCellView(ListAPIView):
    queryset = Blood_Cell.objects.all()
    serializer_class = BloodCellListSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = Blood_Cell.objects.create(file=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)

# Create your views here.
