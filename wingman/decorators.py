from wingman.models import WingmanSettings


def check_feature_flag(flag_name, alt_value=None, alt_func=None):
    """
    A decorator to check a feature flag and either return a value, execute an alternative function,
    or execute the original function.
    :param flag_name: Name of the feature flag (string).
    :param alt_value: Value to return if the feature flag is enabled.
    :param alt_func: Function to return if the feature flag is enabled.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            if WingmanSettings.get_value(flag_name):
                if alt_func:
                    return alt_func(*args, **kwargs)
                if alt_value:
                    return alt_value
            return func(*args, **kwargs)

        return wrapper

    return decorator
