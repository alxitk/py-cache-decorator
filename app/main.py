from typing import Callable


def cache(func: Callable) -> Callable:
    cashe_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        for i in args:
            if args not in cashe_dict:
                cashe_dict[args] = func(*args)
                print("Calculating new result")
                return cashe_dict[args]
            else:
                print("Getting from cache")
                return cashe_dict[args]
    return wrapper
