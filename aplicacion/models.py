from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.
class Categoria(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="categorias")
    icono = models.CharField(max_length=100)
    imagen_promocion = models.ImageField(upload_to="categorias_promo")
    def __str__(self):
        return self.nombre
from django.core.validators import MaxValueValidator, MinValueValidator
class Subcategoria(models.Model):
    nombre= models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="categorias")
    descripcion = models.CharField(max_length=100)
    oferta = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    icono = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,related_name='subcategorias')
    def __str__(self):
        return self.nombre

tipos_productos=[('Físico','Físico'),('Virtual','Virtual')]
class Producto(models.Model):
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100,choices=tipos_productos)
    nombre = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    descripcion =models.TextField()
    marca = models.CharField(max_length=100)
    detalles = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField()
    gratis = models.BooleanField()
    peso = models.IntegerField()
    nombre_icono =models.CharField(max_length=200)
    def __str__(self):
        return self.nombre
from django.core.exceptions import ValidationError 
def file_size(value):
     # add this to some file where you can import it from 
     limit = 2 * 1024 * 1024 
     if value.size > limit: 
         raise ValidationError('File too large. Size should not exceed 2 MiB.') 
class Imagen(models.Model):
    ruta = models.ImageField(upload_to="productos",validators=[file_size])
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE,related_name='imagens')
class Usuario(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="usuarios",blank=True,null=True)
    verificacion = models.BooleanField()
    def __str__(self):
        return self.user.username
class Compra(models.Model):
    costo_envio = models.DecimalField(max_digits=6, decimal_places=2)
    direccion = models.CharField(max_length=300)
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)    
    def __str__(self):
        return str(self.usuario)+" -> "+str(self.fecha)
class DetalleCompra(models.Model):
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra,on_delete=models.CASCADE,related_name='detalles')
    def __str__(self):
        return str(self.cantidad)+"->"+str(self.producto)

class Deseo(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="deseos")
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    def __str__(self):
        return str(self.usuario)+" -> "+str(self.producto)
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    texto = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    def __str__(self):
        return str(self.usuario)+" -> "+str(self.producto)

