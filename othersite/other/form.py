from django import forms
from django.db import models
from models import *
class InformsForm(forms.ModelForm):
	content = forms.CharField(max_length=150)
	
	class Meta:
		model = Post1
class UploadFileForm(forms.Form):
	title = forms.CharField(max_length = 50)
	file = forms.FileField()

class HwForm(forms.ModelForm):
	class Meta:
		model = Hw
		fields = ['title','pic','doc']
