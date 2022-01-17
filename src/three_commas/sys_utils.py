import sys
import inspect
import logging
import functools
from py3cw.request import Py3CW
import os

logger = logging.getLogger(__name__)


def get_parent_function_name() -> str:
    try:
        return sys._getframe(2).f_code.co_name
    except ValueError as e:
        logger.error('Error occurred while fetching the name of the parent.', e)


def get_parent_module_name() -> str:
    """
    give you the name of the parent module. Not the current
    """
    stack_frame = inspect.currentframe()
    while stack_frame:
        if stack_frame.f_code.co_name == '<module>':
            return stack_frame.f_globals['__name__']
        stack_frame = stack_frame.f_back


def logged(*args, use_logger: logging.Logger = None, log_return: bool = False, reduce_long_arguments: bool = False):
    REDUCED_LOGGING_LIMIT = 100

    def reduced_arg(arg):
        arg = str(arg)
        return arg if len(arg) < REDUCED_LOGGING_LIMIT else arg[:REDUCED_LOGGING_LIMIT] + '...'

    if use_logger is None:
        parent_module_name = get_parent_module_name()
        if parent_module_name is None:
            use_logger = logger
        else:
            use_logger = logging.getLogger(parent_module_name)

    def inner(function_to_wrap):
        @functools.wraps(function_to_wrap)
        def wrapper(*args, **kwargs):
            if reduce_long_arguments:
                logging_args = ', '.join([reduced_arg(a) for a in args])
                logging_kwargs = {k: reduced_arg(v) for k, v in kwargs}
            else:
                logging_args = args
                logging_kwargs = kwargs
            use_logger.debug(f"Called '{function_to_wrap.__name__}' with args={logging_args}, kwargs={logging_kwargs}")
            ret = function_to_wrap(*args, **kwargs)
            use_logger.debug(f"Function '{function_to_wrap.__name__}' was executed")
            if log_return:
                use_logger.debug(f"Function '{function_to_wrap.__name__}' returned: {ret}")
            return ret
        return wrapper

    if len(args) == 1 and callable(args[0]):
        return inner(function_to_wrap=args[0])
    return inner


def get_p3cw() -> Py3CW:
    api_key = os.getenv("THREE_COMMAS_API_KEY")
    api_secret = os.getenv("THREE_COMMAS_API_SECRET")
    if api_key is None or api_secret is None:
        raise RuntimeError("Please configure 'THREE_COMMAS_API_KEY' and 'THREE_COMMAS_API_SECRET' in your environment variables")
    return Py3CW(key=api_key, secret=api_secret)


def get_paper_headers():
    return {'Forced-Mode': 'paper'}


def get_real_headers():
    return {'Forced-Mode': 'real'}
