
import sys
sys.path.insert(0,'../')
sys.path.append('/usr/local/lib/python3.7/site-packages')

import platform
print(platform.python_version())

import logging
from logging.config import fileConfig
from imageprocessing.imageporcessing import imageprocessing
from imageprocessing.cycloidDrawings import cycloid
from config.constants import constants
from imageprocessing.monalisa import Mona

if __name__ == "__main__":
    # Init logger
    fileConfig('config/logging_config.ini')
    log = logging.getLogger(__name__)
    log.debug('_main_.py')
    
    # ip = imageprocessing()
    # ip.createImageCustom(1000,1000)
    # ip.cycloidDrawinEllipseInCircle()    

    # ip.saveImage("test")   

    #cy = cycloid()
    #cy.spiral()


    m = Mona()
    m.Generate()
    m.Save()
    



