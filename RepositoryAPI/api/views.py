from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import BeritaSerializer
from .models import Berita
# Create your views here.

class BeritaCrudCBV(ModelViewSet):
    queryset = Berita.objects.order_by('-id')
    serializer_class = BeritaSerializer
    authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
