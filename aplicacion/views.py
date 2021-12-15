from django.shortcuts import render
from .serializers import CategoriaSerializer , SubcategoriaSerializer, ProductoDescuentoSerializer,ProductoSerializer,DeseoSerializer,CompraSerializer,UserSerializer,ComentarioSerializer,UsuarioSerializer, ImagenSerializer, DetalleCompraSerializer, DetalleCompraBestSellerSerializer ,SubcategoriaBestSellerSerializer,ProductosVendidosJuntosSerializer
from .models import Categoria, Subcategoria, Producto, Deseo, Compra, Comentario, Usuario, Imagen, DetalleCompra
from rest_framework import generics, filters  
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

#auth ini
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        usuario = Usuario.objects.filter(user=user)[0]
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': usuario.pk
        })
#auth fin
from django.db.models import Count,Sum
class ProductoBestSeller(generics.ListAPIView):    
    serializer_class= DetalleCompraBestSellerSerializer
    def get_queryset(self):
        detalles = DetalleCompra.objects.all().values('producto','producto__subcategoria').annotate(total=Sum('cantidad')).order_by('-total')
        for i in range(len(detalles)):
            producto = Producto.objects.get(id=detalles[i]['producto'])
            detalles[i]['producto']= producto
            subcategoria = Subcategoria.objects.get(id=detalles[i]['producto__subcategoria'])
            detalles[i]['producto__subcategoria']= subcategoria
        return detalles[:5]
class SubcategoriaBestSeller(generics.ListAPIView):
    
    serializer_class= SubcategoriaBestSellerSerializer
    def get_queryset(self):
        detalles =DetalleCompra.objects.all().values('producto__subcategoria').annotate(total=Sum('cantidad')).order_by('-total')
        for i in range(len(detalles)):
            subcategoria = Subcategoria.objects.get(id=detalles[i]['producto__subcategoria'])
            detalles[i]['producto__subcategoria']= subcategoria
        return detalles[:8]
def take_second(elem):
    return elem['cant']
class ProductosVendidosJuntosR(generics.ListAPIView):    
    serializer_class= ProductoSerializer
    def get_queryset(self):
        compras = Compra.objects.all()
        ids =self.kwargs['id']        
        lista_entregar=[]
        lista =[]
        for i in range(len(compras)):
            detalle = DetalleCompra.objects.filter(compra=compras[i],producto=Producto.objects.get(id=ids))
            if(len(detalle)!=0):
                detalles =DetalleCompra.objects.filter(compra=compras[i])        
                for j in range(len(detalles)):
                    if(detalles[j].id!=detalle[0].id):
                        g=-1
                        for l in range(len(lista)):
                            if(lista[l].get('producto')==detalles[j].producto):  
                                g=l        
                                break
                        if(g==-1):
                            lk = detalles[j].producto
                            obj = {
                                'producto':lk,
                                'cant':1
                            }
                            lista.append(obj)
                        else:                         
                            lista[g]['cant']+=1
                            
        lista =sorted(lista,reverse=True,key=take_second)
        for k in range(len(lista)):
            lista_entregar.append(Producto.objects.get(id=lista[k]['producto'].id))
            
        return lista_entregar[:1]
class ProductosMayorDescuento(generics.ListAPIView):
    serializer_class= ProductoDescuentoSerializer
    def get_queryset(self):
        productos = Producto.objects.all()
        mayor = productos[0]
        for producto in productos:
            if(producto==mayor):
                continue
            if(producto.precio*producto.subcategoria.oferta/100>mayor.precio*mayor.subcategoria.oferta/100):
                mayor=producto
        detalles = DetalleCompra.objects.filter(producto=mayor)
        mayor.vendido=len(detalles)
        return [mayor]

class ProductosMarcaIgual(generics.ListAPIView):
    serializer_class= ProductoSerializer
    def get_queryset(self):
        ids =self.kwargs['id'] 
        producto = Producto.objects.get(id=ids)
        productos = Producto.objects.filter(marca__contains=producto.marca).exclude(id=producto.id)
        return productos
class ProductosVendidosJuntos(generics.ListAPIView):    
    serializer_class= ProductosVendidosJuntosSerializer
    def get_queryset(self):
        compras = Compra.objects.all()
        lista_entregar=[]
        lista =[]
        for i in range(len(compras)):
            detalles =DetalleCompra.objects.filter(compra=compras[i]).values('producto')          
            for j in range(len(detalles)):
                producto = Producto.objects.get(id=detalles[j]['producto'])
                detalles[j]['producto']= producto
                if(j==0):
                    lista.append(list((detalles[j],)))
                else:
                    lista[i].append(detalles[j])
        for j in range(len(lista)-1):
            for i in range(len(lista)-1):
                lista1=lista[j]
                lista2 = lista[i+1]
                for item in lista1:
                    if item in lista2:
                        lista_entregar.append(item)
                if(len(lista_entregar)<=1):
                    lista_entregar=[]
                else:
                    break
            else:
                continue
            break
        return lista_entregar[:8]
class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class SubcategoriaList(generics.ListCreateAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer


class SubcategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

class IsOfertaFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(oferta=True,gratis=False)
class ProductoOfertaList(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = (IsOfertaFilterBackend,)

class IsGratisFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(gratis=True)

class ProductoGratisList(generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = (IsGratisFilterBackend,)

class ProductoList(generics.ListAPIView):
    queryset = Producto.objects.all()
    
    serializer_class = ProductoSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,)
    search_fields = ['nombre','marca']
    filter_fields = ("subcategoria","subcategoria__categoria")
from django.shortcuts import get_object_or_404
class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        productos = Producto.objects.all()
        mayores=[]
        for producto in productos:            
            detalles = DetalleCompra.objects.filter(producto=producto)
            mayor=producto
            mayor.vendido=len(detalles)
            mayores.append(mayor)
        return mayores
    def get_object(self):
        queryset = self.get_queryset()
        pk = int(self.kwargs['pk'])
        for obj in range(len(queryset)):
            if queryset[obj].id == pk:
                return queryset[obj]
        return None
    serializer_class = ProductoDescuentoSerializer

class DeseoList(generics.ListCreateAPIView):
    queryset = Deseo.objects.all()
    serializer_class = DeseoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("usuario","producto")

class DeseoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Deseo.objects.all()
    serializer_class = DeseoSerializer

class CompraList(generics.ListCreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer


class CompraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class ComentarioList(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
#registro ini
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework import status
from django.shortcuts import redirect
@api_view(['POST'])
def create_auth(request):
       serialized = UsuarioSerializer(data=request.data)
       if serialized.is_valid():
                user=User.objects.create_user(
                    username = request.data.get('username'),
                    password = request.data.get('password'),
                    email = request.data.get('email'),
                    first_name= request.data.get('first_name'),
                    last_name=request.data.get('last_name')
                    )
                user.save()
                usuario=Usuario.objects.create(
                    user=user,
                    user_id=user.id,
                    imagen=request.data.get('imagen'),
                    verificacion=request.data.get('verificacion')
                    )
                devolver={
                    "user_id":user.id,
                    "usuario_id":usuario.id
                }
                return redirect("/api/usuarios/"+str(devolver["usuario_id"]))
       else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
import base64
import base64, secrets, io

# django and pillow lib
from PIL import Image
from django.core.files.base import ContentFile
def get_image_from_data_url( data_url, resize=True, base_width=600 ):

    # getting the file format and the necessary dataURl for the file
    _format = "PNG"
    _dataurl       = data_url
    # file name and extension
    _filename, _extension   = secrets.token_hex(20), _format.split('/')[-1]

    # generating the contents of the file
    file = ContentFile( base64.b64decode(_dataurl), name=f"{_filename}.{_extension}")

    # resizing the image, reducing quality and size
    if resize:

        # opening the file with the pillow
        image = Image.open(file)
        # using BytesIO to rewrite the new content without using the filesystem
        image_io = io.BytesIO()

        # resize
        w_percent    = (base_width/float(image.size[0]))
        h_size       = int((float(image.size[1])*float(w_percent)))
        image        = image.resize((base_width,h_size), Image.ANTIALIAS)

        # save resized image
        image.save(image_io, format=_extension)

        # generating the content of the new image
        file = ContentFile( image_io.getvalue(), name=f"{_filename}.{_extension}" )

    # file and filename
    return file, ( _filename, _extension )
@api_view(['POST'])
def create_auth2(request):
        serialized = UsuarioSerializer(data=request.data)
        user=User.objects.create_user(
            username = request.data.get('username'),
            password = request.data.get('password'),
            email = request.data.get('email'),
            first_name= request.data.get('first_name'),
            last_name=request.data.get('last_name')
            )
        user.save()
        avatar_file = get_image_from_data_url(request.data.get('imagen'))[0]
    
        usuario=Usuario.objects.create(
            user=user,
            user_id=user.id,
            imagen=avatar_file,
            verificacion=request.data.get('verificacion')
            )
        devolver={
            "user_id":user.id,
            "usuario_id":usuario.id
        }
        return redirect("/api/usuarios/"+str(devolver["usuario_id"]))
#registro fin

class ImagenList(generics.ListCreateAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("producto",)

class ImagenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializer
    
class DetalleCompraList(generics.ListCreateAPIView):
    queryset = DetalleCompra.objects.all()
    serializer_class = DetalleCompraSerializer

class DetalleCompraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DetalleCompra.objects.all()
    serializer_class = DetalleCompraSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer