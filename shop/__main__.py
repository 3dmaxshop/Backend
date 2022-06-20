import logging

from shop.app import app

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger.info('application start')
    app.run()
