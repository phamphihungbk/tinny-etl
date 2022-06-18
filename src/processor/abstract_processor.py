from datetime import datetime
from logging import Logger

EXTRACT_DATE_FORMAT = '%Y-%m-%d'


class AbstractProcessor:

    def __init__(self, logger: Logger):
        self.logger = logger

    def process(self, record, extract_date, load_date):
        pass

    def add_date_fields(self, record, extract_date, load_date):
        record['extract_date'] = self.date_to_srt(extract_date)
        record['load_date'] = self.date_to_srt(load_date)

    def drop_redundant_fields(self, record, redundant_fields):
        for key in redundant_fields:
            del record[key]

    def date_to_srt(self, date):
        return date.strftime(EXTRACT_DATE_FORMAT)

    def dob_to_age(self, dob, dob_format, extract_date):
        try:
            dob_date = datetime.strptime(dob, dob_format).date()
            delta = extract_date - dob_date
            age = int(delta.days / 365.25)
        except ValueError as err:
            self.logger.warning(
                'dob_to_age() failed to parse dob: {0}'.format(err))
            age = None
        return age
