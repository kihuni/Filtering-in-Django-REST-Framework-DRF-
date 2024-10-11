import django_filters
from .models import Project


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    tech_stack = django_filters.CharFilter(field_name='tech_stack', lookup_expr='icontains')
    created_at = django_filters.DateFilter(field_name='created_at')

    
    class Meta:
        model = Project
        fields = ['name', 'tech_stack', 'created_at']

