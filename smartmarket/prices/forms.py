
from django import forms


class SearchForm(forms.Form):
    search_input = forms.CharField(label='Buscar', max_length=100)
