from functools import wraps
from django.contrib import messages
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required

default_message = "Please log in, in order to see the requested page."


def user_passes_test(test_func, message=default_message):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not test_func(request.user):
                messages.info(request, message)  # change this to error
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


def login_required_message(function=None, message=default_message):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated,
        message=message,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def login_required_message_and_redirect(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None,
                                        message=default_message):
    if function:
        return login_required_message(
            login_required(function, redirect_field_name, login_url),
            message
        )

    return lambda deferred_function: login_required_message_and_redirect(deferred_function, redirect_field_name,
                                                                         login_url, message)
