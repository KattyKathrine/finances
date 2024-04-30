from django import forms
from .models import Record, Item

class RecordForm(forms.ModelForm):

    date = forms.DateField(widget = forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Record
        fields = [
            'date',
            'text',
            'sum',
            'includes_items',
            'is_income',
            'category',

        ]

class ShopForm(forms.ModelForm):

    date = forms.DateField(widget = forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Record
        fields = [
            'date',
            'text',
            'sum',
            'category',

        ]


class ItemForm(forms.ModelForm):

   class Meta:
       model = Item
       fields = [
           'name',
           'record',
           'cost',
           'amount',
           'category',

       ]
