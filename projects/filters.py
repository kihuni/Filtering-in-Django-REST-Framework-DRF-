import django_filters
from .models import Project


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    tech_stack = django_filters.CharFilter(field_name='tech_stack', lookup_expr='icontains')
    
    # Define separate filters for date range
    created_at_after = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_at_before = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')

    
    class Meta:
        model = Project
        fields = ['name', 'tech_stack', 'created_at']

