from django.db import models

# Create your models here.
class Slide(models.Model):
    img_fondo = models.ImageField(upload_to="img_fondo_slide")
    tipo_slide = models.CharField(max_length=100)
    img_producto = models.ImageField(upload_to="img_producto_slide")
    estilo_img_producto = models.CharField(max_length=100)
    estilo_texto_slide = models.CharField(max_length=100)
    titulo1 = models.CharField(max_length=100)
    titulo2 = models.CharField(max_length=100)
    titulo3 = models.CharField(max_length=100)
    boton = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    def __str__(self):
        return self.titulo1
class Plantilla(models.Model):
    barra_superior = models.CharField(max_length=200)
    texto_superior = models.CharField(max_length=100)
    color_fondo = models.CharField(max_length=100)
    color_texto = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="logo_plantilla")
    icono = models.ImageField(upload_to="icono_plantilla")
    redes_sociales = models.CharField(max_length=100)
    fecha = models.DateTimeField()
class Banner(models.Model):
    ruta = models.CharField(max_length=100)
    img = models.ImageField(upload_to="banners")
    titulo1 = models.CharField(max_length=100)
    titulo2 = models.CharField(max_length=100)
    titulo3 = models.CharField(max_length=100)
    estilo = models.CharField(max_length=100)
    fecha = models.DateTimeField()