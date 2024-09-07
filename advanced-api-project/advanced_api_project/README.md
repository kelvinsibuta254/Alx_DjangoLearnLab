# Custom Views
### built using generic views and mixins

## Views
### Is a function that takes a web request and returns a response
### It is basically the connection between the client and the server

## Generic Views
### Allow you to quickly build api views that map closely to the database models.
### Encapsulate common patterns for CRUD operations
### Provide default implementations for handling HTTP methods like GET, POST, PUT, PATCH, and DELETE
### Abstract away repetitive code
### Promote code reuse
### In order to create custom views with generics, define a class that inherits from the GenericAPIView class.
### This class extends from the APIView class, adding required behaviour for standard list and detail views

## Mixins
#### Are re-usable pieces of code that add functionality to views
#### can be combined with generic views to add specific behaviors such as authentication, permission checks and custom logic
#### provide action methods rather than handler methods such as .get() and .post()

### ListModelMixin
#### .list(request, *args, **kwargs) implements listing a queryset

### CreateModelMixin
#### .create(request, *args, **kwags) implements creating and saving a new model instance

### RetrieveModelMixin
#### .retrieve(request, *args, **kwargs) implements returning an existing model instance in a response

### UpdateModelMixin
#### .update(request, *args, **kwargs) implements updating and saving an existing model instance
#### .partialupdate(request, *args, **kwargs) all fields for the update will be optional

### DestroyModelMixin
#### .destroy(request, *args, **kwargs) implements deletion of an existing model instance

### To implement Mixins, create a separate class for each mixin and then inherit it within the class where you want to incorporate the functionality.