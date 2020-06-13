import datetime, inspect, itertools, numbers, time
from typing import Callable, Dict, List, Tuple

from .. import config

def nonnegative(*params) -> Callable:
    def inner(func) -> Callable:
        def wrapper(*args, **kwargs) -> Callable:
            args_names: Tuple = inspect.getfullargspec(func)[0]
            args_dict: Dict = dict(zip(args_names, args))

            for p in params:
                if p not in args_dict:
                    continue

                v: object = args_dict[p]
                if isinstance(v, numbers.Number) and v < 0:
                    raise ValueError(f"Argument '{p}' has a negative value of {v}.")
            return func(*args, **kwargs)
        return wrapper
    return inner

def timer(func) -> Callable:
    def inner(*args, **kwargs) -> Callable:
        start: float = time.time()
        result: object = func(*args, **kwargs)
        end: float = time.time()

        if config.DEBUG:
            print(f"{func.__name__}: {(end - start) * 1000} ms.")
        
        return result
    return inner

#region utility functions
def str_to_bool(val: str) -> bool:
    true_values: List = {"Y", "YES", "TRUE"}
    return val.upper() in true_values

def ms_to_datetime(val: str) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(val / 1000)
#endregion