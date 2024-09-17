from django import forms
from .models import Inflow


class InflowForm(forms.ModelForm):

    class Meta:
        model = Inflow
        fields = ['supplier', 'product', 'quantity', 'description']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control', 'rows': '3'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'rows': '3'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }
        labels = {
            'name': 'Fornecedor',
            'description': 'Produto',
            'description': 'Quantidade',
            'description': 'Descrição',
        }
