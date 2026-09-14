"""MAIN файл - основная логика программы."""

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def main():
    logger.info('START')
    # TODO: основная программа
    x = 1

    logger.info('STOP')


if __name__ == '__main__':
    main()
