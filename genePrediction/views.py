from django.shortcuts import render
import numpy as np
import pandas as pd
from Bio.Seq import Seq
from Bio import SeqIO
from .OpenReadingFrame import findPotentialCodingSegments
from basicClassesAndForms.forms import UploadFileForm
from os import system

def home(request):
    return render(request,'genePrediction/gene_prediction.html',{'form' : UploadFileForm()})

def predict(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['file']
            with open('fasta.txt', 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            record_iterator = SeqIO.parse('fasta.txt',"fasta")
            system("rm fasta.txt")
            record1 = next(record_iterator)
            sq = str(record1.seq)
            stopList = [i for i in range(len(sq)) if (sq.startswith('TGA',i) or sq.startswith('TAG',i) or sq.startswith('TAA',i))]
            orfs = findPotentialCodingSegments(sq,stopList)

            context = {
	            'orfs':orfs
            }
            return render(request,'genePrediction/open_reading_frame.html',context)
        else:
            return render(request,'genePrediction/gene_prediction.html',{'form' : UploadFileForm()})
    else:
        return render(request,'genePrediction/gene_prediction.html',{'form' : UploadFileForm()})