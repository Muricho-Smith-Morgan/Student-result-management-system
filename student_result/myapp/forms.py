from django import forms
from .models import Mark

class EditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    year = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    mark = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    
    
    class Meta:
        model = Mark
        fields = '__all__'



class EditStudentInfoForm(forms.ModelForm):
   
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    year = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    mark = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    
    
    class Meta:
        model = Mark
        fields = '__all__'

class EditCaseInfoForm(forms.ModelForm):
  
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    year = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    mark = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
   
    class Meta:
        model = Mark
        fields = '__all__'




class EditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    year = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
    mark = forms.CharField(widget=forms.TextInput(attrs={'type': 'text'}))
   
    class Meta:
        model = Mark
        fields = '__all__'