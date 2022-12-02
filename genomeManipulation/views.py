import imp
from django.shortcuts import render
from matplotlib.style import context
from basicClassesAndForms.forms import GenomeSequenceInputForm
from basicClassesAndForms.models import GenomeSequence
from .translation import translate
from .reverse_complement import reverseComplement
from .protein_synthesis import computeProteinChain

def genomeManipulationHome(request):
    return render(request,'genomeManipulation/home.html')


def translation(request):
    form = GenomeSequenceInputForm(request.POST) 

    if request.method == 'POST':
        form = GenomeSequenceInputForm(request.POST)
        if form.is_valid():
            genomeSequence = form.cleaned_data.get("sequence")
            
            context = {
                'translated_sequence' : translate(genomeSequence),
                'form': form
            }

            return render(request,'genomeManipulation/translation.html',context)
            
        else:
            form = GenomeSequenceInputForm()
    return render(request,'genomeManipulation/translation.html',{'form': form})
    
def reverseComplementView(request):
    form = GenomeSequenceInputForm(request.POST) 

    if request.method == 'POST':
        form = GenomeSequenceInputForm(request.POST)
        if form.is_valid():
            genomeSequence = form.cleaned_data.get("sequence")
            
            context = {
                'reversed_sequence' : reverseComplement(genomeSequence),
                'form': form
            }

            return render(request,'genomeManipulation/reverse_complement.html',context)

            
        else:
            form = GenomeSequenceInputForm()
    return render(request,'genomeManipulation/reverse_complement.html',{'form': form})

def proteinSynthesisView(request):
    form = GenomeSequenceInputForm(request.POST) 

    if request.method == 'POST':
        form = GenomeSequenceInputForm(request.POST)
        if form.is_valid():
            genomeSequence = form.cleaned_data.get("sequence")
            
            context = {
                'converted_sequence' : computeProteinChain(genomeSequence),
                'form': form
            }

            return render(request,'genomeManipulation/protein_synthesis.html',context)

            
        else:
            form = GenomeSequenceInputForm()
    return render(request,'genomeManipulation/protein_synthesis.html',{'form': form})