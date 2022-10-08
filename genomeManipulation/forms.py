from django import forms
from .models import GenomeSequence

class TranslationForm(forms.ModelForm):
	class Meta:
		model = GenomeSequence
		fields = ['genomeSequence']