from logging import Logger, getLogger, INFO


class ServiceFactory:

	@staticmethod
	def get_logger(name: str) -> Logger:
		logger = getLogger(name)
		logger.setLevel(INFO)

		return logger
