from enum import Enum


class AbstractThreeCommasEnum(Enum):
    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        else:
            return super.__eq__(self, other)

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    def __str__(self):
        return self.value


class BotScope(AbstractThreeCommasEnum):
    ENABLED = 'enabled'
    DISABLED = 'disabled'


class DealScope(AbstractThreeCommasEnum):
    ACTIVE = 'active'
    FINISHED = 'finished'
    COMPLETED = 'completed'
    CANCELED = 'cancelled'
    FAILED = 'failed'


class ForcedMode(AbstractThreeCommasEnum):
    PAPER = 'paper'
    REAL = 'real'

