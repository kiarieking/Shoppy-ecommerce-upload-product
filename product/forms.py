from django import forms

class AddProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    cost = forms.IntegerField()
    Description = forms.Textarea()
