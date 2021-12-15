from django.contrib import admin
from .models import Banner,Slide, Plantilla
# Register your models here.
admin.site.register(Banner)
admin.site.register(Slide)
admin.site.register(Plantilla)


admin.site.site_header = 'TECSHOP'