# Creating Custom Mixins
class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple 
    field filtering based on a 'lookup_fields' attribute, 
    instead of the default single field
    """
    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field):
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj