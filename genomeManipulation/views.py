import imp
from django.shortcuts import render
from matplotlib.style import context
from .forms import TranslationForm
from .models import GenomeSequence
from .translation import translate


def genomeManipulationHome(request):
    return render(request,'genomeManipulation/home.html')


def translation(request):
    form = TranslationForm(request.POST) 

    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            form.save()
            genomeSequence = form.cleaned_data.get("genomeSequence")
            
            context = {
                'translated_sequence' : translate(genomeSequence),
                'form': form
            }

            return render(request,'genomeManipulation/translation.html',context)
            
        else:
            form = TranslationForm()
    return render(request,'genomeManipulation/translation.html',{'form': form})