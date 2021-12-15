from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^slides/$', views.SlideList.as_view()),
    url(r'^slides/(?P<pk>[0-9]+)/$', views.SlideDetail.as_view()),

    url(r'^plantillas/$', views.PlantillaList.as_view()),
    url(r'^plantillas/(?P<pk>[0-9]+)/$', views.PlantillaDetail.as_view()),

    url(r'^banners/$', views.BannerList.as_view()),
    url(r'^banners/(?P<pk>[0-9]+)/$', views.BannerDetail.as_view()),
]
