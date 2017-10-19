import builtins
from  functools import wraps, partial
from datetime import datetime

raw_print = builtins.print


def new_print(*args, print_msg=True, **kwargs):
    if print_msg:
        raw_print(*args)
    return raw_print(datetime.now().strftime("%Y-%m-%d %H:%M"), *args, **kwargs)


def print_to_log(log_file, print_msg=True):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(log_file, "a", encoding="utf8") as f:
                builtins.print = partial(new_print, print_msg=print_msg, file=f)
                res = func(*args, **kwargs)
                builtins.print = raw_print
            return res

        return wrapper

    return decorate

