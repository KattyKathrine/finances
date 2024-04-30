from django_filters import FilterSet, NumberFilter, DateFilter, DateTimeFilter, ModelMultipleChoiceFilter
from .models import Record, Category
from django import forms
from datetime import date


class RecordFilter(FilterSet):

    date__gt = DateTimeFilter(field_name='date', lookup_expr='gt', label='От', widget=forms.TextInput(attrs={
        'type': 'date', 'min': '2022-08-25'}))

    date__lt = DateTimeFilter(field_name='date', lookup_expr='lt', label='До', widget=forms.TextInput(attrs={
        'type': 'date', 'max': date.today()}))

    category__icontains = ModelMultipleChoiceFilter(field_name='category', label='Категория', queryset=Category.objects.all())

    #record_month = DateFilter(field_name='date', lookup_expr='month', label='Месяц',
    #                          widget=forms.SelectDateWidget(months=MONTHS))

    class Meta:
        model = Record
        fields = {
            #'date': ['month']
            #'category': ['icontains'],
        }