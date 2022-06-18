import os
import csv
import json
from datetime import datetime
from logging import Logger

from src.transformer import EXTRACT_DATE_FORMAT


def date_to_dir(extract_date) -> str:
    return os.path.join('{0}'.format(extract_date.year),
                        '{:02}'.format(extract_date.month),
                        '{:02}'.format(extract_date.day))


class Extractor:
    def __init__(self, logger: Logger):
        self.logger = logger

    def extract(self, data_dir: str, extract_date: str) -> list:
        generator = []
        extract_date = datetime.strptime(extract_date, EXTRACT_DATE_FORMAT).date()

        data_dir = os.path.join(data_dir, date_to_dir(extract_date))
        files = os.listdir(data_dir)

        if len(files) == 0:
            self.logger.error('No data for date: {0}'.format(extract_date))
            return generator

        for file in files:
            filepath = os.path.join(data_dir, file)

            if filepath.endswith('.csv'):
                generator.append(Extractor.read_csv(filepath, limit=0))
            elif filepath.endswith('.json'):
                generator.append(Extractor.read_json(filepath, limit=0))

            self.logger.info('Read from {0}'.format(filepath))

        return generator

    @staticmethod
    def read_json(filename: str, limit: int = 0):
        count = 0
        with open(filename) as json_file:
            line = json_file.readline()
            while line:
                yield json.loads(line)
                line = json_file.readline()
                count += 1
                if not limit and count >= limit:
                    break

    @staticmethod
    def read_csv(filename: str, limit: int = 0):
        count = 0
        with open(filename) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                yield row
                count += 1
                if not limit and count >= limit:
                    break
