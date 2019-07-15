import sys
sys.path.insert(0,'../')

import logging
from imageprocessing.imageporcessing import imageprocessing
from config.constants import constants

class cycloid:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug('__init__()')

    def interLoopQuadCircles(self):
        self.log.debug("interLoopQuadCircles()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)
        ip.cycloidDrawingSection()
        ip.rotateImage(30)
        ip.cycloidDrawingSection()
        ip.rotateImage(30)
        ip.cycloidDrawingSection()
        ip.rotateImage(30)
        ip.cycloidDrawingSection()
        ip.saveImage('interLoopQuadCircles')    

    def circleWithinACircle(self):
        self.log.debug("circleWithinACircle()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)
        ip.cycloidDrawing(100,[600,500],0,200,4,1)
        ip.rotateImage()
        ip.cycloidDrawing(100,[200,500],0,-70,-4,1)
        ip.saveImage("circleWithinACircle")

    def fancyLetterS(self):
        self.log.debug("fancyLetterS()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)
        ip.cycloidDrawing(100,[640,306],0,200,4,1,35)
        ip.rotateImage(180)
        ip.cycloidDrawing(100,[637,308],0,200,4,1,35)
        ip.saveImage("fancyLetterS")

    def sudarshanChakra(self):
        self.log.debug("fancyLetterS()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)
        ip.cycloidDrawing(100,[640,306],0,200,4,1,35)
        ip.rotateImage(20)
        ip.cycloidDrawing(100,[637,308],0,200,4,1,35)
        ip.rotateImage(20)
        ip.cycloidDrawing(100,[640,306],0,200,4,1,25)
        ip.rotateImage(20)
        ip.cycloidDrawing(100,[637,308],0,200,4,1,25)
        ip.rotateImage(20)
        ip.cycloidDrawing(100,[637,308],0,200,4,1,25)
        ip.rotateImage(20)
        ip.cycloidDrawing(100,[640,306],0,200,4,1,25)
        ip.rotateImage(20)
        ip.cycloidDrawing(100,[637,308],0,200,4,1,25)
        ip.rotateImage(20)
        ip.cycloidDrawing(100,[637,308],0,200,4,1,25)
        ip.rotateImage(20)
        ip.cycloidDrawing(100,[640,306],0,200,4,1,25)
        ip.rotateImage(20)
        ip.cycloidDrawing(100,[637,308],0,200,4,1,25)
        ip.saveImage("sudarshanChakra")

    def owlEyes(self):
        self.log.debug("owlEyes()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)
        ip.cycloidDrawing(100,[400,500],0,100,4,1,13)
        ip.rotateImage(90)
        ip.cycloidDrawing(100,[500,400],0,100,4,1,13)
        ip.rotateImage(90)
        ip.cycloidDrawing(100,[400,500],0,100,4,1,13) 
        ip.rotateImage(90)
        ip.cycloidDrawing(100,[500,400],0,100,4,1,13)

        ip.cycloidDrawing(1,[590,400],0,20,2,1,10)
        ip.cycloidDrawing(1,[590,600],0,20,2,1,10)
        ip.saveImage("owlEyes")    

    def animalHorn(self):
        self.log.debug("animalHorn()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)
        ip.cycloidDrawingCircleIncreaseInCircle(20,180)
        ip.saveImage("animalHorn")

    def swirlWithCircles(self):
        self.log.debug("swirlWithCircles()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)
        ip.cycloidDrawingCircleIncreaseInCircle(20,180)
        ip.rotateImage(90)
        ip.cycloidDrawingCircleIncreaseInCircle(20,180)
        ip.rotateImage(90)
        ip.cycloidDrawingCircleIncreaseInCircle(20,180)
        ip.rotateImage(90)
        ip.cycloidDrawingCircleIncreaseInCircle(20,180)
        ip.saveImage("swirlWithCircles")

    def crownWithCircles(self):
        self.log.debug("crownWithCircles()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)
        ip.cycloidDrawingCircleIncreaseInCircle(10,50)
        ip.saveImage("crownWithCircles")

    def neverEndingCone(self):
        self.log.debug("neverEndingCone()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)
        ip.cycloidDrawingCircleIncreaseInCircle(10,120)
        ip.rotateImage(60)
        ip.cycloidDrawingCircleIncreaseInCircle(10,120,1)    
        ip.saveImage("neverEndingCone")    

    def womanFaceBigHair(self):
        self.log.debug("womanFaceBigHair()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)
        ip.cycloidDrawingCircleConeLowHighLow(10,180)
        ip.saveImage("womanFaceBigHair")

    def sphericalIllusion(self):
        self.log.debug("sphericalIllusion()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)
        ip.cycloidDrawinEllipseInCircle()
        ip.saveImage("sphericalIllusion")

    def EllipticalIllusion(self):
        self.log.debug("EllipticalIllusion()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([400,400],200,1,1,10,180,100,1.2,0.5,False,1,0,100,1)
        ip.cycloidDrawinEllipseInCircle([600,600],200,1,1,10,288,100,1.2,0.5,False,1,0,100,1)
        ip.cycloidDrawinEllipseInCircle([600,400],150,1,1,10,288,100,1.2,0.5,False,1,0,100,3)
        ip.cycloidDrawinEllipseInCircle([400,600],100,1,1,10,288,75,1.2,0.5,False,1,0,100,3)
        ip.saveImage("EllipticalIllusion")    

    def EllipticalPortionIllution(self):
        self.log.debug("EllipticalPortionIllution()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([500,500],200,1,1,10,288,100,1.2,0.5,False,1,0,100,1)
        ip.cycloidDrawinEllipseInCircle([500,500],200,1,1,50,288*4,100,1.2,0.5,False,1,0,100,0)
        ip.rotateImage(90,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([500,500],200,1,1,10,288,100,1.2,0.5,False,1,0,100,1)
        ip.cycloidDrawinEllipseInCircle([500,500],200,1,1,50,288*4,100,1.2,0.5,False,1,0,100,0)
        ip.rotateImage(90,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([500,500],200,1,1,50,288*4,100,1.2,0.5,False,1,0,100,0)
        ip.rotateImage(90,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([500,500],200,1,1,50,288*4,100,1.2,0.5,False,1,0,100,0)
        ip.saveImage("EllipticalPortionIllution")

        
    def EllipticalPortionHalfHalf(self):
        self.log.debug("EllipticalPortionHalfHalf()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000,constants.WHITE_COLOR)

        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,60,288*2,140,1.2,0.5,False,1,0,100,1)
        ip.rotateImage(180,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,60,288*2,140,1.2,0.5,False,1,0,100,1)

        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,50,288*4,100,1.2,0.5,False,1,0,100,3)
        ip.rotateImage(180,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,50,288*4,100,1.2,0.5,False,1,0,100,3)

        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,40,288*2,60,1.2,0.5,False,1,0,100,3)
        ip.rotateImage(180,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,40,288*2,60,1.2,0.5,False,1,0,100,3)

        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,35,288*2,20,1.2,0.5,False,1,0,100,3)
        ip.rotateImage(180,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,35,288*2,20,1.2,0.5,False,1,0,100,3)

        ip.saveImage("EllipticalPortionHalfHalf")

    def EllipticalPortionHalfHalfReverse(self):
        self.log.debug("EllipticalPortionHalfHalfReverse()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000,constants.WHITE_COLOR)

        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,35,288*2,140,1.2,0.5,False,1,0,100,1)
        ip.rotateImage(180,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,35,288*2,140,1.2,0.5,False,1,0,100,1)

        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,40,288*4,100,1.2,0.5,False,1,0,100,3)
        ip.rotateImage(180,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,40,288*4,100,1.2,0.5,False,1,0,100,3)

        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,50,288*2,60,1.2,0.5,False,1,0,100,3)
        ip.rotateImage(180,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,50,288*2,60,1.2,0.5,False,1,0,100,3)

        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,60,288*2,20,1.2,0.5,False,1,0,100,3)
        ip.rotateImage(180,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,60,288*2,20,1.2,0.5,False,1,0,100,3)

        ip.saveImage("EllipticalPortionHalfHalfReverse")   

    def EllipticalPortionHalfHalfVarient(self):
        self.log.debug("EllipticalPortionHalfHalfVarient()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)#,constants.WHITE_COLOR)

        ip.cycloidDrawinEllipseInCircle([605,670],200,1,1,15,288*1,140,1.2,0.5,True,1,0,100,1)
        ip.rotateImage(180)#,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([605,670],200,1,1,15,288*1,140,1.2,0.5,True,1,0,100,1)

        ip.cycloidDrawinEllipseInCircle([605,670],200,1,1,30,288*2,100,1.2,0.5,True,1,0,100,4)
        ip.rotateImage(180)#,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([605,670],200,1,1,30,288*2,100,1.2,0.5,True,1,0,100,4)

        ip.cycloidDrawinEllipseInCircle([605,670],200,1,1,50,288*4,100,1.2,0.5,True,1,0,100,3)
        ip.rotateImage(180)#,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircle([605,670],200,1,1,50,288*4,100,1.2,0.5,True,1,0,100,3)

        # ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,60,288*2,20,1.2,0.5,False,1,0,100,3)
        # ip.rotateImage(180,constants.WHITE_COLOR)
        # ip.cycloidDrawinEllipseInCircle([300,500],200,1,1,60,288*2,20,1.2,0.5,False,1,0,100,3)

        ip.saveImage("EllipticalPortionHalfHalfVarient") 

    def EllipticalRotateSpring(self):
        self.log.debug("EllipticalRotateSpring()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)#,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircleRotaion([500,500],200,1,1,5,144*1,100,1.2,0.5,False,1,0,100,True,5,1)
        ip.saveImage("EllipticalRotateSpring") 

    def EllipticalRotateAtom(self):
        self.log.debug("EllipticalRotateAtom()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)#,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircleRotaion([500,500],200,1,1,1,144*1,100,1.2,0.5,False,1,0,100,True,5,0)
        ip.saveImage("EllipticalRotateAtom") 

    def EllipticalRotateOverlaps(self):
        self.log.debug("EllipticalRotateOverlaps()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)#,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircleRotaion([500,500],200,1,1,9,144*1,130,1.2,0.5,False,1,0,100,True,15,1)
        ip.saveImage("EllipticalRotateOverlaps") 


    def EllipticalRotateOverlapsHD(self):
        self.log.debug("EllipticalRotateOverlaps()")
        ip = imageprocessing()
        ip.createImageCustom(2000,2000)#,constants.WHITE_COLOR)
        ip.cycloidDrawinEllipseInCircleRotaion([1000,1000],400,1,1,9,144*1,130,1.2,0.5,False,1,0,100,True,15,1)
        ip.cycloidDrawinEllipseInCircleRotaion([1000,1000],400,1,1,9,144*1,130,1.2,0.5,False,1,0,100,True,15,1)
        ip.cycloidDrawinEllipseInCircleRotaion([1000,1000],200,1,1,9,144*1,130,1.2,0.5,False,1,0,100,True,15,4)
        # ip.cycloidDrawinEllipseInCircleRotaion([500,500],150,1,1,7,144*1,70,1.2,0.5,False,1,0,100,True,20,2)
        ip.saveImage("EllipticalRotateOverlaps") 

    # ip.cycloidDrawinEllipseInCircleRotaion([500,500],150,1,1,1,144*4,70,1.2,0.5,False,1,0,100,True,20,2)
    # ip.cycloidDrawinEllipseInCircleRotaion([500,500],100,1,1,10,144*1,130,1.2,0.5,False,1,0,100,True,5,4)


    def spiral(self):
        self.log.debug("spiral()")
        ip = imageprocessing()
        ip.createImageCustom(1000,1000)#,constants.WHITE_COLOR)
        ip.spiralDrawing()
        ip.saveImage("spiral") 
