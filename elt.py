import argparse
import os
from datetime import datetime

from src.utils.service_factory import ServiceFactory
from src.extractor import Extractor
from src.loader import Loader
from src.transformer import Transformer
from src.processor.factory import ProcessorFactory

DATA_DIR = 'data'


def main():
	logger = ServiceFactory.get_logger('tinny-etl')

	parser = argparse.ArgumentParser(add_help=False, description='Tinny ETL')
	parser.add_argument('game', type=str, help='Name of the game')
	parser.add_argument('date', type=str, help='Extract date in format YYYY-MM-DD')

	args = parser.parse_args()
	args.game = args.game.lower()
	args.date = args.date.lower()

	data_dir = os.path.join(DATA_DIR, args.game)
	logger.info('Start ETL for game {0}'.format(args.game))

	processor = ProcessorFactory.create(args.game, logger)

	# instantiate object
	extractor = Extractor(logger)
	transformer = Transformer(logger, processor)
	loader = Loader(logger)

	extracted_data = extractor.extract(data_dir, args.date)
	transformed_data = transformer.transform(extracted_data, args.date, datetime.today())
	loader.load(transformed_data, args.game)

	logger.info('Finish ETL for game {0}'.format(args.game))


if __name__ == '__main__':
	main()
