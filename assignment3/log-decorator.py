# Task 1: Writing and Testing a Decorator

# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        if args:
            logger.log(logging.INFO, f"positional parameters: {args}")
        else:
            logger.log(logging.INFO, "positional parameters: none")
        if kwargs:
            logger.log(logging.INFO, f"keyword parameters: {kwargs}")
        else:
            logger.log(logging.INFO, "keyword parameters: none")
        logger.log(logging.INFO, f"return: {result}")
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

