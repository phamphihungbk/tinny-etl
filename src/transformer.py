from datetime import datetime
from logging import Logger

from src.processor.abstract_processor import AbstractProcessor

EXTRACT_DATE_FORMAT = '%Y-%m-%d'


class Transformer:

    def __init__(self, logger: Logger, processor: AbstractProcessor):
        self.logger = logger
        self.processor = processor

    def transform(self, data, extract_date, load_date):
        self.logger.info('Transform data')
        extract_date = datetime.strptime(extract_date, EXTRACT_DATE_FORMAT).date()

        res = []
        for item in data:
            res += map(
                lambda record: self.processor.process(record, extract_date, load_date), item)

        return res
