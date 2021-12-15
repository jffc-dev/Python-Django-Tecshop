from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^categorias/$', views.CategoriaList.as_view()),
    url(r'^categorias/(?P<pk>[0-9]+)/$', views.CategoriaDetail.as_view()),

    url(r'^subcategorias/$', views.SubcategoriaList.as_view()),
    url(r'^subcategorias/(?P<pk>[0-9]+)/$', views.SubcategoriaDetail.as_view()),
    url(r'^subcategorias/bestseller/$',views.SubcategoriaBestSeller.as_view()),

    url(r'^productos/$', views.ProductoList.as_view()),
    url(r'^productos/(?P<pk>[0-9]+)/$', views.ProductoDetail.as_view()),
    url(r'^productos/oferta/',views.ProductoOfertaList.as_view()),
    url(r'^productos/gratis/',views.ProductoGratisList.as_view()),
    url(r'^productos/bestseller/$',views.ProductoBestSeller.as_view()),
    url(r'^productos/juntos/$',views.ProductosVendidosJuntos.as_view()),
    url(r'^productos/juntos/(?P<id>[0-9]+)/$',views.ProductosVendidosJuntosR.as_view()),
    url(r'^productos/marca/(?P<id>[0-9]+)/$',views.ProductosMarcaIgual.as_view()),    
    url(r'^producto/oferta/$',views.ProductosMayorDescuento.as_view()),    

    url(r'^usuarios/$', views.UsuarioList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view()),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^compras/$', views.CompraList.as_view()),
    url(r'^compras/(?P<pk>[0-9]+)/$', views.CompraDetail.as_view()),

    url(r'^deseos/$', views.DeseoList.as_view()),
    url(r'^deseos/(?P<pk>[0-9]+)/$', views.DeseoDetail.as_view()),

    url(r'^comentarios/$', views.ComentarioList.as_view()),
    url(r'^comentarios/(?P<pk>[0-9]+)/$', views.ComentarioDetail.as_view()),

    url(r'^imagenes/$', views.ImagenList.as_view()),
    url(r'^imagenes/(?P<pk>[0-9]+)/$', views.ImagenDetail.as_view()),

    url(r'^detalles/$', views.DetalleCompraList.as_view()),
    url(r'^detalles/(?P<pk>[0-9]+)/$', views.DetalleCompraDetail.as_view()),

    url(r'^register/',views.create_auth),
    url(r'^register2/',views.create_auth2),

    url(r'^auth/',views.CustomAuthToken.as_view()),
    
]