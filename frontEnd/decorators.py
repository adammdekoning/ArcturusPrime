from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_function):
    def decorator_function(request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('frontEnd:dashboard')

        else:
            return view_function(request, *args, **kwargs)

    return decorator_function

def coach_restricted(allowed_roles=['Coach', 'Coordinator']):
    def decorator(view_function):
        def wrapper_function(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_function(request, *args, **kwargs)
            else:
                return redirect('frontEnd:dashboard')

        return wrapper_function
    return decorator
