from functools import wraps


def decorator(original_function):
    @wraps(original_function)
    def decorated_function(*args, **kwargs):
        return original_function(*args, **kwargs)

    return decorated_function
