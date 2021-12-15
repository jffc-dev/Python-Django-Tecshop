from rest_framework import serializers
from .models import Categoria , Imagen, Subcategoria, Producto, Deseo, Compra, Comentario, Usuario, DetalleCompra
from django.contrib.auth.models import User

        
class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields=('id','nombre','imagen','descripcion','oferta','icono','categoria')
        depth=1
class CategoriaSerializer(serializers.ModelSerializer):
    subcategorias = SubcategoriaSerializer(many=True,read_only=True)
    class Meta:
        model = Categoria
        fields=('id','nombre','descripcion','imagen','imagen_promocion','icono','subcategorias')

class ImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagen
        fields = ('id','ruta','producto')
class ProductoDescuentoSerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(many=True,read_only=True,source="imagens")
    vendido = serializers.IntegerField()
    class Meta:
        model = Producto
        fields=('id','imagenes','tipo','nombre','marca','titulo','descripcion','detalles','precio',
        'stock','gratis','vendido','peso','subcategoria')
        depth=1
        
class ProductoSerializer(serializers.ModelSerializer):
    imagenes = ImagenSerializer(many=True,read_only=True,source="imagens")
    class Meta:
        model = Producto
        fields=('id','imagenes','tipo','nombre','marca','titulo','descripcion','detalles','precio',
        'stock','gratis','peso','subcategoria')
        depth=1
class DeseoSerializer(serializers.ModelSerializer):
    producto =ProductoSerializer(read_only=True)
    producto_id = serializers.IntegerField(write_only=True)
    usuario_id = serializers.IntegerField(write_only=True)
    class Meta:
        model= Deseo
        fields=('id','fecha','usuario_id','producto','producto_id')

class DetalleCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model= DetalleCompra
        fields =('id','cantidad','producto','compra')
class CompraSerializer(serializers.ModelSerializer):
    detalles = DetalleCompraSerializer(many=True,read_only=True)
    class Meta:
        model=Compra
        fields=('id','costo_envio','direccion','fecha','usuario','detalles')
class SubcategoriaBestSellerSerializer(serializers.ModelSerializer):
    subcategoria = SubcategoriaSerializer(source="producto__subcategoria")
    total = serializers.IntegerField()
    class Meta:
        model= DetalleCompra
        fields =('subcategoria','total')
        depth=1
class DetalleCompraBestSellerSerializer(serializers.ModelSerializer):
    subcategoria = SubcategoriaSerializer(source="producto__subcategoria")
    producto = ProductoSerializer()
    total = serializers.IntegerField()
    class Meta:
        model= DetalleCompra
        fields =('producto','total','subcategoria')
        depth=1
class ProductosVendidosJuntosSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()
    class Meta:
        model= DetalleCompra
        fields =('producto',)
        depth=1
        
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields=('id','texto','fecha','usuario','producto')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.set_password ( validated_data.get('password',instance.password))
        instance.save()
        return instance
class UsuarioSerializer(serializers.ModelSerializer):    
    user_id=serializers.IntegerField(write_only=True)
    deseos = DeseoSerializer(many=True,read_only=True)
    class Meta:
        model = Usuario
        fields=('id','user_id','imagen','verificacion','user','deseos')
        depth=1
        
