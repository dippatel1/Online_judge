from django import forms

class SubmitedCode(forms.Form):
   solution = forms.CharField(widget=forms.Textarea)

