from django.contrib import admin
from core.models import Evento

# Register your models here.

class evento_admin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',)

admin.site.register(Evento, evento_admin)

