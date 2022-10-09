from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.genomeManipulationHome,name='home'),
    path('translation/',views.translation,name='translation' ),
    path('reverse_complement/',views.reverse_complement,name='reverse_complement' ),
]
