import re
from typing import List
from dataclasses import dataclass, field
import logging
import json

logger = logging.getLogger(__name__)


class ThreeCommasError(RuntimeError):
    @dataclass
    class BoToSmallError:
        # matches: List[tuple] = field(default_factory=lambda: list())
        amount: float = None # field(default_factory=lambda: list())
        pair: str = None # field(default_factory=lambda: list())
        # present: bool = False

    BO_TO_SMALL_ERROR_PATTERN = re.compile(r"Base order size is too small\. Min: ([0-9.]*),? ?([\w_]+)?", re.IGNORECASE)
    NO_MARKET_PAIR_ERROR_PATTERN = re.compile(r"No market data for this pair: ([^\']*)\'", re.IGNORECASE)
    EXTRACT_PY3CW_MESSAGE_PATTERN = re.compile(r"Other error occurred: record_invalid Invalid parameters (\{.*\})\.", re.IGNORECASE)
    BOT_WAS_DELETED_ERROR_PATTERN = re.compile(r"Other error occurred: Not found None None", re.IGNORECASE)
    BOT_DID_NOT_EXISTED_OR_BELONGS_TO_OTHER_ACCOUNT_ERROR_PATTERN = re.compile(r"Other error occurred: not_found Not Found None", re.IGNORECASE)

    def __init__(self, error):
        self.error: dict = error
        self.error_parsed: dict = None
        try:
            if self._has_error_message():
                match = ThreeCommasError.EXTRACT_PY3CW_MESSAGE_PATTERN.findall(error.get('msg'))
                if match:
                    self.error_parsed = eval(match[0])
        except:
            logger.warning(f'Failed to parse inner error msg {error}')

    def bo_to_small_error(self) -> (float, str):
        ret = list()
        # ret = ThreeCommasError.BoToSmallError(present=False)
        if self._has_parsed_error_message() and self.error_parsed.get('base_order_volume'):
            # ret.present = True
            for sub_message in self.error_parsed.get('base_order_volume'):
                bo_min_match = ThreeCommasError.BO_TO_SMALL_ERROR_PATTERN.findall(sub_message)
                if bo_min_match:
                    amount = float(bo_min_match[0][0])
                    pair = bo_min_match[0][1] or None
                    ret.append(ThreeCommasError.BoToSmallError(amount=amount, pair=pair))
                    #ret.matches.append((amount, pair))
                    # ret.amount.append(float(bo_min_match[0][0]))
                    # ret.pair.append(bo_min_match[0][1] or None)

        return ret

    def is_no_market_pair_error(self) -> List[str]:
        if self._has_error_message():
            pairs_to_remove = ThreeCommasError.NO_MARKET_PAIR_ERROR_PATTERN.findall(self.error.get('msg'))
            if pairs_to_remove:
                return pairs_to_remove

    def is_not_found_error(self):
        return self._has_error_message() and 'not_found' in self.error.get('msg') or 'Not found' in self.error.get('msg')

    def _has_error_message(self):
        return self.error and self.error.get('msg')

    def _has_parsed_error_message(self):
        return self.error_parsed

    def __repr__(self):
        return f'{self.__class__}({self.error.get("msg")})'
