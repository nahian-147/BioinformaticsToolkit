from django.contrib import admin

from django.urls import path

from . import views

urlpatterns = [
    
    path('translation/',views.translation,name='translation' ),

    path('reverse_complement/',views.reverseComplementView,name='reverseComplementView'),

    path('protein_synthesis/',views.proteinSynthesisView,name='proteinSynthesisView'),
]
