from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        widgets = {
            'item': forms.TextInput(attrs={ 'size': '20'}),  
            'quantidade': forms.NumberInput(attrs={'size': '15'}),
            
            'gramatura': forms.TextInput(attrs={ 'size': '20'}),    
            'valor_referencia': forms.NumberInput(attrs={'size': '8'}),
            'valor_minimo': forms.NumberInput(attrs={ 'size': '10'}),
            'valor_arrematado': forms.NumberInput(attrs={'size': '15'}),
            'margem': forms.NumberInput(attrs={'class': 'custom-input', 'size': '20'}),       
            'valor_total': forms.NumberInput(attrs={'class': 'custom-input', 'size': '20'}),
            'ganhador': forms.TextInput(attrs={'class': 'custom-input', 'size': '20'}), 
            'marca': forms.TextInput(attrs={'class': 'custom-input', 'size': '40'}), 
            'obs': forms.TextInput(attrs={'class': 'custom-input', 'size': '40'}), 
        }