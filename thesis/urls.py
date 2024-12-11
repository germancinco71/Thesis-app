from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('med/', views.med, name="med"),
    path('medlist/<int:id>/', views.medabs, name="medlist"),
    path('it/', views.it, name="it"),
    path('itlist/<int:id>', views.itabs, name="itlist"),
    path('cs/', views.cs, name="cs"),
    path('cslist/<int:id>/', views.csabs, name="cslist"),
    
]