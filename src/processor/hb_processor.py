from logging import Logger

from src.processor.abstract_processor import AbstractProcessor

DROP_FIELDS_HB = ['id', 'first_name', 'last_name', 'email', 'ip_address', 'dob']
HB_DOB_FORMAT = '%m/%d/%Y'


class HBProcessor(AbstractProcessor):

    def __init__(self, logger: Logger):
        super().__init__(logger)

    def process(self, record, extract_date, load_date):
        record['accountid'] = record['email']
        record['country'] = record['ip_address']
        record['age'] = self.dob_to_age(record['dob'], HB_DOB_FORMAT, extract_date)
        record['gender'] = record['gender'].lower()
        record['game'] = 'hb'
        self.add_date_fields(record, extract_date, load_date)
        self.drop_redundant_fields(record, DROP_FIELDS_HB)

        return record
