from django.shortcuts import render
from .serializers import BannerSerializer,PlantillaSerializer, SlideSerializer
from .models import Banner, Plantilla, Slide
from rest_framework import generics
# Create your views here.
class BannerList(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


class BannerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class PlantillaList(generics.ListCreateAPIView):
    queryset = Plantilla.objects.all()
    serializer_class = PlantillaSerializer


class PlantillaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plantilla.objects.all()
    serializer_class = PlantillaSerializer

class SlideList(generics.ListCreateAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer


class SlideDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer
