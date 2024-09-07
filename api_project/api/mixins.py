class AllowPUTAsCreateMixin(object):
    """
    The following mixin class may be used in order to support PUT-as-create
    behavior for incoming requests.
    """
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object_or_none()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        if instance is None:
            lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
            lookup_value = self.kwargs[lookup_url_kwarg]
            extra_kwargs = {self.lookup_field: lookup_value}
            serializer.save(**extra_kwargs)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def get_object_or_none(self):
        try:
            return self.get_object()
        except Http404:
            if self.request.method == 'PUT':
    """For PUT-as-create operation, we need to ensure that we have relevant permissions, as if this was a POST request.
    This will either raise a PermissionDenied exception, or simply return None."""
                self.check_permissions(clone_request(self.request, 'POST'))
            else:
    """PATCH requests where the object does not exist should still return a 404 response."""
                raise

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
        obj = get_object_or_404(Book, pk=pk, **filter)
        self.check_object_permissions(self.request, obj)
        return obj