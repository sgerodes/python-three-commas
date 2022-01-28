import os
import logging


logger = logging.getLogger(__name__)


def check_bool_env(env_var_name: str, default_value: bool) -> bool:
    default_value_str = str(default_value).upper()
    var = os.getenv(env_var_name, default_value_str)
    if var.upper() in {'TRUE', 'FALSE'}:
        return var.upper() == 'TRUE'
    else:
        logger.warning(f"boolean variable {env_var_name} value is not set to a boolean. "
                       f"Should be in {{'TRUE', 'FALSE'}} but is '{var}', Will default to {default_value_str}")
        return default_value_str.upper() == 'TRUE'


THREE_COMMAS_AUTO_PARSE_DEFAULT = check_bool_env('THREE_COMMAS_AUTO_PARSE_DEFAULT', True)
THREE_COMMAS_AUTO_PARSE_DATETIME_DEFAULT = check_bool_env('THREE_COMMAS_AUTO_PARSE_DATETIME_DEFAULT', False)
THREE_COMMAS_LOG_API = check_bool_env('THREE_COMMAS_LOG_API_DEFAULT', True)  # will log only on debug level
REDUCED_LOGGING_LIMIT = 130
