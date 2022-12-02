from django import forms

class GenomeSequenceInputForm(forms.Form):
	sequence = forms.CharField(max_length=999999999)


class UploadFileForm(forms.Form):
    file = forms.FileField()