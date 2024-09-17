from django import forms
from .models import Outflow


class OutflowForm(forms.ModelForm):

    class Meta:
        model = Outflow
        fields = ['product', 'quantity', 'description']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control', 'rows': '3'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'rows': '3'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }
        labels = {
            'description': 'Produto',
            'description': 'Quantidade',
            'description': 'Descrição',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')

        if quantity > product.quantity:
            raise forms.ValidationError(
                f'A quantidade disponível para o produto {product.title} é de {product.quantity} unidades.'
            )

        return quantity