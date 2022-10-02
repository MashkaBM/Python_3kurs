

def author(name = '...'):
    def decorator(func):
        def wrapper(*args, **kwargs): #наша обёртка
        
            wrapper._author = name
            return func(*args, **kwargs)

        return wrapper

    return decorator
