import builtins
from  functools import wraps, partial
from datetime import datetime

older_print = builtins.print


def new_print(*args, **kwargs):
    return older_print(datetime.now().strftime("%Y-%m-%d %H:%M"), *args, **kwargs)


def print_to_log(log_file):
    def decorate(func):
        @wraps(partial)
        def wrapper(*args, **kwargs):
            with open(log_file, "a", encoding="utf8") as f:
                builtins.print = partial(new_print, file=f)
                res = func(*args, **kwargs)
                builtins.print = older_print
                return res

        return wrapper

    return decorate
