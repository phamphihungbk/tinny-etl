from logging import Logger

from src.processor.hb_processor import HBProcessor
from src.processor.wwc_processor import WWCProcessor


class ProcessorFactory:

	@staticmethod
	def create(name: str, logger: Logger):
		if name == 'hb':
			return HBProcessor(logger)
		elif name == 'wwc':
			return WWCProcessor(logger)
		else:
			logger.error('No processor return')
			return None
