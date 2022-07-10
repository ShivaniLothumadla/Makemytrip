import softest
import logging


class Utils(softest.TestCase):

    def assertListItems(self, List, value):
        for i in List:
            self.soft_assert(self.assertIn, value, i.text)
            print('Pass', end=' ')

    def logger(self):
        # create a logger
        logger = logging.getLogger(__name__)
        # set the level
        logger.setLevel(logging.INFO)
        # create console handler or file handler
        ch = logging.StreamHandler()
        fh = logging.FileHandler(filename='log1.log')
        # create format
        formater = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
        # set format to the handlers
        ch.setFormatter(formater)
        fh.setFormatter(formater)
        # add handler to the logger
        logger.addHandler(ch)
        logger.addHandler(fh)
        # return logger
        return logger