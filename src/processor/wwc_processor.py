from logging import Logger

from src.processor.abstract_processor import AbstractProcessor

WWC_DOB_FORMAT = '%Y-%m-%d %H:%M:%S'
DROP_FIELDS_WWC = ['name', 'location', 'email', 'login', 'registered', 'phone',
                   'cell', 'picture', 'dob', 'nat', 'id']


class WWCProcessor(AbstractProcessor):

	def __init__(self, logger: Logger):
		super().__init__(logger)

	def process(self, record, extract_date, load_date):
		record['accountid'] = record['login']['username']
		record['country'] = record['nat']
		record['age'] = self.dob_to_age(record['dob'], WWC_DOB_FORMAT, extract_date)
		record['gender'] = record['gender'].lower()
		record['game'] = 'wwc'
		self.add_date_fields(record, extract_date, load_date)
		self.drop_redundant_fields(record, DROP_FIELDS_WWC)
		return record
