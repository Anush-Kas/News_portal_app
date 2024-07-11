from django_filters import FilterSet, CharFilter, DateTimeFilter
from django import forms
from .models import Post


class PostFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains', label='Title')
    postCategory = CharFilter(lookup_expr='exact', label='Category')
    dateCreation = DateTimeFilter(lookup_expr='gt', label='Date',
                                  widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Post
        fields = [
            'title',
            'postCategory',
            'dateCreation',
        ]
