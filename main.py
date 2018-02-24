
import logging
from logging.config import fileConfig

import sys
sys.path.insert(0,'../')


if __name__ == "__main__":
    # Init logger
    fileConfig('config/logging_config.ini')
    log = logging.getLogger(__name__)
    log.debug('_main_.py')
    