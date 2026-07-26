# Task 1: Writing and Testing a Decorator

# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if args:
            positional = f"positional parameters: {args}"
        else:
            positional = "positional parameters: none"
        if kwargs:
            keyword = f"keyword parameters: {kwargs}"
        else:
            keyword = "keyword parameters: none"
        
        log_entry = (
            f"function: {func.__name__}\n"
            f"{positional}\n"
            f"{keyword}\n"
            f"return: {result}"
        )

        logger.log(logging.INFO, log_entry)

        return result 
    return wrapper 

@logger_decorator
def hello():
    print("Hello, World!")

@logger_decorator
def manyArgs(*args):
    return True 

@logger_decorator
def manyKwargs(**kwargs):
    return logger_decorator

hello()
manyArgs(1)
manyKwargs(name="Fisher", role="Student")

