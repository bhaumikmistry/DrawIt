import sys
sys.path.insert(0,'../')

import logging
from imageprocessing.imageporcessing import imageprocessing
from config.constants import constants


class Mona:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug('__init__()')
        self.ip = imageprocessing()

    def Generate(self):
        self.log.debug("interLoopQuadCircles()")
        ip = self.ip
        ip.createImageCustom(1000,1000)
        

        #  add line of the frame
        ip.drawLine(100,200,100,800,constants.COLORS_I_DEMAND,2)
        ip.drawLine(100,800,900,800,constants.COLORS_I_DEMAND,2)
        ip.drawLine(900,800,900,200,constants.COLORS_I_DEMAND,2)
        ip.drawLine(900,200,100,200,constants.COLORS_I_DEMAND,2)

        # ip.drawSequenceCircle(
        #     x0=50,
        #     y0=50,
        #     x1=50,
        #     y1=950,
        #     frequencyCenters=10,
        #     radius=50,
        #     colors=constants.COLORS_I_DEMAND,
        #     colorKey=4,
        #     portion=1
        #     )

        # ip.drawSequenceCircle(
        #     x0=50,
        #     y0=50,
        #     x1=950,
        #     y1=50,
        #     frequencyCenters=10,
        #     radius=50,
        #     colors=constants.COLORS_I_DEMAND,
        #     colorKey=4,
        #     portion=1
        #     )

        # ip.drawSequenceCircle(
        #     x0=50,
        #     y0=150,
        #     x1=950,
        #     y1=150,
        #     frequencyCenters=10,
        #     radius=50,
        #     colors=constants.COLORS_I_DEMAND,
        #     colorKey=4,
        #     portion=1
        #     )

        # ip.drawSequenceCircle(
        #     x0=950,
        #     y0=50,
        #     x1=950,
        #     y1=950,
        #     frequencyCenters=10,
        #     radius=50,
        #     colors=constants.COLORS_I_DEMAND,
        #     colorKey=4,
        #     portion=1
        #     )


        # ip.drawSequenceCircle(
        #     x0=950,
        #     y0=950,
        #     x1=50,
        #     y1=950,
        #     frequencyCenters=10,
        #     radius=50,
        #     colors=constants.COLORS_I_DEMAND,
        #     colorKey=4,
        #     portion=1
        #     )

        # ip.drawSequenceCircle(
        #     x0=950,
        #     y0=850,
        #     x1=50,
        #     y1=850,
        #     frequencyCenters=10,
        #     radius=50,
        #     colors=constants.COLORS_I_DEMAND,
        #     colorKey=4,
        #     portion=1
        #     )

        ip.drawSequenceCircle(
            x0=115,
            y0=215,
            x1=885,
            y1=215,
            frequencyCenters=10,
            radius=15,
            colors=constants.COLORS_I_DEMAND,
            colorKey=3,
            portion=1
            )

    def Save(self, name="MonaLisa"):
        self.ip.saveImage(name)   

