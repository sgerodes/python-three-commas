import sys
import inspect
import logging

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