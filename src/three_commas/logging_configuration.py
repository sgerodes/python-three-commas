import logging
import logging.config
import logging.handlers
import functools
from .sys_utils import get_parent_module_name

logger = logging.getLogger(__name__)


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
