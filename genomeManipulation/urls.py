from django.contrib import admin

from django.urls import path

from . import views

jls_extract_var = [
    path('',views.genomeManipulationHome,name='home'),

    path('translation/',views.translation,name='translation' ),

    path('reverse_complement/',views.reverseComplementView,name='reverseComplementView'),

    path('protein_synthesis/',views.proteinSynthesisView,name='proteinSynthesisView'),
urlpatterns = jls_extract_var
