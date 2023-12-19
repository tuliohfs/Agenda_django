from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Agenda/', views.lista_eventos),
    path('Agenda/lista/', views.json_lista_eventos),
    path('Agenda/evento/', views.evento),
    path('Agenda/evento/submit', views.submit_evento),
    path('Agenda/eventos/delete/<int:id_evento>/', views.delete_evento),
    path('', views.index),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),
    path('logout/', views.logout_user),

]
