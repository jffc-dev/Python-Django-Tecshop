from rest_framework import serializers
from .models import Slide
from .models import Plantilla
from .models import Banner

class SlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slide
        fields=('id','img_fondo','tipo_slide','img_producto','estilo_img_producto','estilo_texto_slide','titulo_1','titulo_2','titulo_3','boton','url','fecha')

class PlantillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plantilla
        fields=('id','img_fondo','tipo_slide','img_producto','estilo_img_producto','estilo_texto_slide','titulo_1','titulo_2','titulo_3','boton','url','fecha')

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields=('id','ruta','img','titulo1','titulo2','titulo3','estilo','fecha')