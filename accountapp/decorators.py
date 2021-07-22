from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_owership_decorator(func):
    def decorated(request, *args, **kwargs):
        target_name = User.objects.get(pk=kwargs['pk'])

        if target_name == request.user:
            return func(request, *args, **kwargs)

        else:
            return HttpResponseForbidden()


    return decorated