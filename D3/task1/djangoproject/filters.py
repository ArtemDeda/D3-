import django_filters
from django import forms
from .models import News


class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Название')
    category = django_filters.CharFilter(lookup_expr='iexact', label='Категория')
    published_after = django_filters.DateFilter(
        field_name='date_published',
        label='Дата публикации',
        widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = News
        fields = ['title', 'category', 'published_after']