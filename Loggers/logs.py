import logging


class Logger:
    def test_logger(self):
        # create logger
        logger = logging.getLogger('demo')

        # set logger level
        logger.setLevel(logging.DEBUG)

        # create console or file handler
        ch = logging.StreamHandler()
        fh = logging.FileHandler('demologgers.log')

        # create format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')

        # set format
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # add handler to the logger
        logger.addHandler(ch)
        logger.addHandler(fh)

        # write loggers
        logger.debug('debug: this is debug msg.')
        logger.info('info: this is info msg.')
        logger.critical('critical: this is critical msg.')
        logger.error('error: this is error msg.')
        logger.warning('warning: this is warning msg.')

dl = Logger()
dl.test_logger()
