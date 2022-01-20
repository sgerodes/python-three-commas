from .enums import AbstractStringEnum


class DealStatus(AbstractStringEnum):
	ACTIVE = 'active'
	FINISHED = 'finished'
	COMPLETED = 'completed'
	CANCELLED = 'cancelled'
	FAILED = 'failed'

	def is_active(self) -> bool:
		return self == DealStatus.ACTIVE

	def is_finished(self) -> bool:
		return self == DealStatus.FINISHED

	def is_completed(self) -> bool:
		return self == DealStatus.COMPLETED

	def is_cancelled(self) -> bool:
		return self == DealStatus.CANCELLED

	def is_failed(self) -> bool:
		return self == DealStatus.FAILED
