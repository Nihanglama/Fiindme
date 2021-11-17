from django.http import HttpResponse


def permissions(allowed_to=[]):
          def decorator(function):
                    def wrapper(request,*args, **kwargs):

                              group=None
                              if request.user.groups.exists():
                                        group=request.user.groups.all()[0].name
                              if group in allowed_to:
                                        return function(request,*args, **kwargs)
                              else:
                                        return HttpResponse('<h1>403 Forbidden</h1>')
                    return wrapper
          return decorator

