
import sys
sys.path.insert(0,'../')

import logging
from logging.config import fileConfig
from imageprocessing.imageporcessing import imageprocessing


if __name__ == "__main__":
    # Init logger
    fileConfig('config/logging_config.ini')
    log = logging.getLogger(__name__)
    log.debug('_main_.py')
    
    ip = imageprocessing()
    ip.createImage()
    ip.galaxyPattern()
    ip.saveImage('test')



