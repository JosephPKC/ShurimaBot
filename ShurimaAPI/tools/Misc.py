import inspect, itertools, numbers, time
from typing import Callable, Dict, Tuple

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

def timer(should_print: bool) -> Callable:
    def inner(func) -> Callable:
        def wrapper(*args, **kwargs) -> Callable:
            start: float = time.time()
            result: object = func(*args, **kwargs)
            end: float = time.time()

            if should_print:
                print(f"{func.__name__}: {end - start} ms.")
            
            return result
        return wrapper
    return inner
    

    
    

