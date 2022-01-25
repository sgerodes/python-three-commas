import re
from typing import List
from dataclasses import dataclass, field
import logging
import json

logger = logging.getLogger(__name__)


@dataclass
class BaseOrderToSmallErrorElement:
    amount: float = None
    pair: str = None


class ThreeCommasError(RuntimeError):

    BO_TO_SMALL_ERROR_PATTERN = re.compile(r"Base order size is too small\. Min: ([0-9.]*),? ?([\w_]+)?", re.IGNORECASE)
    NO_MARKET_PAIR_ERROR_PATTERN = re.compile(r"No market data for this pair: ([^\']*)\'", re.IGNORECASE)
    EXTRACT_PY3CW_MESSAGE_PATTERN = re.compile(r"Other error occurred: record_invalid Invalid parameters (\{.*\})\.", re.IGNORECASE)
    BOT_WAS_DELETED_ERROR_PATTERN = re.compile(r"Other error occurred: Not found None None", re.IGNORECASE)
    BOT_DID_NOT_EXISTED_OR_BELONGS_TO_OTHER_ACCOUNT_ERROR_PATTERN = re.compile(r"Other error occurred: not_found Not Found None", re.IGNORECASE)
    API_KEY_NOT_ENOUGH_PERMISSION_PATTERN = re.compile(r"access_denied Api key doesn't have enough permissions", re.IGNORECASE)
    API_KEY_INVALID_OR_EXPIRED_PATTERN = re.compile(r'api_key_invalid_or_expired Unauthorized. Invalid or expired api key', re.IGNORECASE)

    def __init__(self, error):
        self.error: dict = error

    def is_api_key_has_no_permission_error(self) -> bool:
        return self._has_error_message() and self.API_KEY_NOT_ENOUGH_PERMISSION_PATTERN.findall(self.get_msg())

    def is_api_key_invalid_or_expired(self) -> bool:
        return self._has_error_message() and self.API_KEY_INVALID_OR_EXPIRED_PATTERN.findall(self.get_msg())

    def is_base_order_to_small_error(self) -> bool:
        return self._has_error_message() and self.BO_TO_SMALL_ERROR_PATTERN.findall(self.get_msg())

    def is_not_found_error(self) -> bool:
        return self._has_error_message() and 'not_found' in self.get_msg() or 'Not found' in self.get_msg()

    def is_no_market_pair_error(self) -> List[str]:
        return self._has_error_message() and self.NO_MARKET_PAIR_ERROR_PATTERN.findall(self.get_msg())

    def get_no_market_pair_error(self) -> List[str]:
        if self._has_error_message():
            pairs_to_remove = ThreeCommasError.NO_MARKET_PAIR_ERROR_PATTERN.findall(self.error.get('msg'))
            if pairs_to_remove:
                return pairs_to_remove
        return list()

    def get_base_order_to_small_error(self) -> List[BaseOrderToSmallErrorElement]:
        ret = list()
        if self._has_error_message():
            try:
                match = ThreeCommasError.EXTRACT_PY3CW_MESSAGE_PATTERN.findall(self.get_msg())
                if match:
                    error_parsed = eval(match[0])
                else:
                    return list()
            except:
                return list()
            if error_parsed.get('base_order_volume'):
                for sub_message in error_parsed.get('base_order_volume'):
                    bo_min_match = ThreeCommasError.BO_TO_SMALL_ERROR_PATTERN.findall(sub_message)
                    if bo_min_match:
                        amount = float(bo_min_match[0][0])
                        pair = bo_min_match[0][1] or None
                        ret.append(BaseOrderToSmallErrorElement(amount=amount, pair=pair))
        return ret

    def _has_error_message(self):
        return self.error and self.get_msg()

    def get_msg(self):
        return self.error.get('msg')

    def __repr__(self):
        return f'{self.__class__.__name__}({self.error})'


