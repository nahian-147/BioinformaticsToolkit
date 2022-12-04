from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('basicClassesAndForms.urls')),
    path('genome_manipulation/', include('genomeManipulation.urls')),
    path('gene_prediction/', include('genePrediction.urls')),
]
