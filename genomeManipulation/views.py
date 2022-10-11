import imp
from django.shortcuts import render
from matplotlib.style import context
from .forms import TranslationForm
from .models import GenomeSequence
from .translation import translate
from .forms import ReverseComplementForm
from .reverse_complement import reverseComplement


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
    
def reverseComplementView(request):
    form = ReverseComplementForm(request.POST) 

    if request.method == 'POST':
        form = ReverseComplementForm(request.POST)
        if form.is_valid():
            form.save()
            genomeSequence = form.cleaned_data.get("genomeSequence")
            
            context = {
                'reversed_sequence' : reverseComplement(genomeSequence),
                'form': form
            }

            return render(request,'genomeManipulation/reverse_complement.html',context)

            
        else:
            form = ReverseComplementForm()
    return render(request,'genomeManipulation/reverse_complement.html',{'form': form})

def proteinSynthesisView(request):
    form = ProteinSynthesisForm(request.POST) 

    if request.method == 'POST':
        form = ProteinSynthesisForm(request.POST)
        if form.is_valid():
            form.save()
            genomeSequence = form.cleaned_data.get("genomeSequence")
            
            context = {
                'converted_sequence' : findPotentialCodingSegments(genomeSequence),
                'form': form
            }

            return render(request,'genomeManipulation/protein_synthesis.html',context)

            
        else:
            form = ProteinSynthesisForm()
    return render(request,'genomeManipulation/protein_synthesis.html',{'form': form})