import sys
sys.path.insert(0,'../')

import logging
import cv2
import numpy as np
from config.constants import constants
import random
import math

class imageprocessing:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug('__init__()')

    def createImage(self):
        self.blank_image = np.zeros((constants.HEIGHT*constants.HEIGHT,constants.WIDTH*constants.WIDTH,constants.CHANNELRGB), np.uint8)
        self.h = len(self.blank_image)
        self.w = len(self.blank_image[0])

    def createImageCustom(self,width,height,background=constants.BLACK_COLOR):
        self.w = width
        self.h = height  
        self.blank_image = np.zeros((self.h,self.w,constants.CHANNELRGB), np.uint8)
        if background is constants.WHITE_COLOR:
            self.blank_image.fill(255)
  
    def saveImage(self,name='m'):
        """
        saveImage for the current object, 
        default name is m.png
        arg :
        name -> string # name of the file without extension.
        """
        self.name = ""
        self.name = name
        cv2.imwrite('{}.png'.format(name),self.blank_image)
    
    def rotateImage(self,angle=180,color=constants.BLACK_COLOR):
        colorImage = self.blank_image
        num_rows, num_cols = colorImage.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), angle, 1)
        cv2.warpAffine(colorImage, rotation_matrix, (num_cols, num_rows),colorImage,cv2.INTER_LINEAR,cv2.BORDER_CONSTANT,color)
        self.blank_image = colorImage
        
    def paintWhite(self):
        colorImage = self.blank_image
        for i in range(self.h):
            for j in range(self.w):
                if (colorImage[i,j,0] == 0 &
                    colorImage[i,j,1] == 0 &
                    colorImage[i,j,2] == 0 ):
                    colorImage[i,j,0] = 255
                    colorImage[i,j,1] = 255
                    colorImage[i,j,2] = 255
        self.blank_image = colorImage        

    def spiralDrawing(self):
        self.log.debug("spiralDrawing")
        colorImage = self.blank_image
        axisPixelFactor = 20
        axisCirclePotion = 1
        colors = constants.COLORS_PANTONE_COOL

        h = len(colorImage)
        w = len(colorImage[0])        

        center = [500,500]

        xCenter = center[0]
        yCenter = center[1]
        key = random.randint(0, len(colors)-1)
        r = 10
        rr = 25.0

        for i in range(0,int(36000*1.5),1 * axisPixelFactor):
            key = random.randint(0, len(colors)-1)
            # axis circle portion decides the part of circle to show up
            angle = i/axisCirclePotion  

            x1 = int(angle/15*math.cos(angle * math.pi /1800))
            y1 = int(angle/15*math.sin(angle * math.pi /1800))

            if x1>center[0]-1:
                break
            if y1>center[1]-1:
                break
                
            # colorImage = self.blank_image
            # colors = constants.COLORS
            # key = random.randint(0, 9)
            rr=rr+0.2
            for j in range(0,36000,1):
                angle = j/1
                xx1 = int(rr * math.cos(angle * math.pi /180))
                yy1 = int(rr * math.sin(angle * math.pi /180))

                # color pixel
                value = colors['{}'.format(key)]

                if xCenter+x1+xx1>h-1 or xCenter+x1+xx1<0 :
                    continue
                if yCenter+y1+yy1>w-1 or yCenter+y1+yy1<0 :
                    continue

                colorImage[xCenter+x1+xx1,yCenter+y1+yy1,0] = value[0]
                colorImage[xCenter+x1+xx1,yCenter+y1+yy1,1] = value[1]
                colorImage[xCenter+x1+xx1,yCenter+y1+yy1,2] = value[2]

            value = colors['{}'.format(key)]
            colorImage[xCenter+x1,yCenter+y1,0] = value[0]
            colorImage[xCenter+x1,yCenter+y1,1] = value[1]
        self.colorImage = colorImage



    def cycloidDrawinEllipseInCircleRotaion(self,
        center=[500,500],           # center for axis circle
        radiusAxisCicle=250,        # cetner for counter circle
        widthForAxisEllipse=1,
        heightForAxisEllipse=1,
        axisCirclePotion=10,
        axisPixelFactor=180,        # number of pixels on the axis = number of counter circles
        radiusCounterCircle=50,     # radius for counter cirle 
        widthForCounterEllipse=3,
        heightForCounterEllipse=0.7,
        radiusChangeFlag=False,     # radius counter fluctuation flag
        offsetIncrementFactor=1,     # change the factor to make different design axisPixleFactor [36,0.1] [72,0.2] and so on
        counterCircleAngle=0,
        counterCirclePortion=100,
        rotateFlag=False,
        offsetAlphaIncrement=1,
        kKey=1):
        """
        Plain Ellipse drawing on canvas with appropriate angle,
        radius, and roate angle.

        Args:
            center ([int,int]) : center of the ellipse (x,y) pixel location.
            radius (int) : Radius for the ellipse.
            xAngle (float) : Combines with radius to give width of the ellipse.
            yAngle (float) : Combines wiht radius to give height of the ellipse.
            alpha (int) : Degree of roation given the ellipse from the center.

        """
        self.log.debug("cycloidDrawingEllipse")
        colorImage = self.blank_image
        colors = constants.COLORS_I_DEMAND
        
        xCenter = center[0]
        yCenter = center[1]

        key = random.randint(0, len(colors)-1)
        if kKey is not None:
            key = kKey

        self.log.debug(key)

        offset = 0
        rotateCounterAlpha = 0
        offsetAlpha = 0
        offsetMax = radiusCounterCircle

        # degrees for bigger circle
        # range(
        #       x       = starting 
        #       y       = maximum number of steps needed to cover every point
        #                 on the cirlce with Width of 250 pixels
        #       steps   = the lower the steps the better the circle looks with
        #                 of circle made up of pixels 
        #       )
        for i in range(0,36000,1 * axisPixelFactor):
            
            # axis circle portion decides the part of circle to show up
            angle = i/axisCirclePotion  

            x1 = int(heightForAxisEllipse * radiusAxisCicle * math.cos(angle * math.pi /1800))
            y1 = int(widthForAxisEllipse * radiusAxisCicle * math.sin(angle * math.pi /1800))
            
            if radiusChangeFlag:
                radiusCounterCircle = 10+offset
                if offset < offsetMax:
                    offset = offset + offsetIncrementFactor
                else:
                    offset=0

            if rotateFlag:
                rotateCounterAlpha = 0+offsetAlpha
                if offsetAlpha < 360:
                    offsetAlpha = offsetAlpha + offsetAlphaIncrement
                else:
                    offsetAlpha=0


            value = colors['{}'.format(key)]
            colorImage[xCenter+x1,yCenter+y1,0] = value[0]
            colorImage[xCenter+x1,yCenter+y1,1] = value[1]
            colorImage[xCenter+x1,yCenter+y1,2] = value[2]
            for j in range(0,3600,1):                
                xxCenter = xCenter + x1
                yyCenter = yCenter + y1

                aangle = j
                xx1 = int(heightForCounterEllipse * radiusCounterCircle * math.cos(aangle * math.pi /1800))
                yy1 = int(widthForCounterEllipse * radiusCounterCircle * math.sin(aangle * math.pi /1800))

                if rotateCounterAlpha is not 0:
                    xr1 = int(xx1 * math.cos(rotateCounterAlpha*math.pi /360) - yy1 * math.sin(rotateCounterAlpha*math.pi /360))
                    yr1 = int(xx1 * math.sin(rotateCounterAlpha*math.pi /360) + yy1 * math.cos(rotateCounterAlpha*math.pi /360))
                else:
                    xr1=xx1
                    yr1=yy1

                # color pixel
                value = colors['{}'.format(key)]
                colorImage[xxCenter+xr1,yyCenter+yr1,0] = value[0]
                colorImage[xxCenter+xr1,yyCenter+yr1,1] = value[1]
                colorImage[xxCenter+xr1,yyCenter+yr1,2] = value[2]
        

        self.colorImage = colorImage

    def cycloidDrawinEllipseInCircle(self,
        center=[500,500],           # center for axis circle
        radiusAxisCicle=250,        # cetner for counter circle
        widthForAxisEllipse=1,
        heightForAxisEllipse=1,
        axisCirclePotion=10,
        axisPixelFactor=180,        # number of pixels on the axis = number of counter circles
        radiusCounterCircle=50,     # radius for counter cirle 
        widthForCounterEllipse=3,
        heightForCounterEllipse=0.7,
        radiusChangeFlag=False,     # radius counter fluctuation flag
        offsetIncrementFactor=1,     # change the factor to make different design axisPixleFactor [36,0.1] [72,0.2] and so on
        counterCircleAngle=0,
        counterCirclePortion=100,
        kKey=1):
        """
        Plain Ellipse drawing on canvas with appropriate angle,
        radius, and roate angle.

        Args:
            center ([int,int]) : center of the ellipse (x,y) pixel location.
            radius (int) : Radius for the ellipse.
            xAngle (float) : Combines with radius to give width of the ellipse.
            yAngle (float) : Combines wiht radius to give height of the ellipse.
            alpha (int) : Degree of roation given the ellipse from the center.

        """
        self.log.debug("cycloidDrawingEllipse")
        colorImage = self.blank_image
        colors = constants.COLORS_PANTONE_COOL
        
        xCenter = center[0]
        yCenter = center[1]

        key = random.randint(0, len(colors)-1)
        if kKey is not None:
            key = kKey

        self.log.debug(key)

        offset = 0

        offsetMax = radiusCounterCircle

        # degrees for bigger circle
        # range(
        #       x       = starting 
        #       y       = maximum number of steps needed to cover every point
        #                 on the cirlce with Width of 250 pixels
        #       steps   = the lower the steps the better the circle looks with
        #                 of circle made up of pixels 
        #       )
        for i in range(0,36000,1 * axisPixelFactor):
            
            # axis circle portion decides the part of circle to show up
            angle = i/axisCirclePotion  

            x1 = int(heightForAxisEllipse * radiusAxisCicle * math.cos(angle * math.pi /1800))
            y1 = int(widthForAxisEllipse * radiusAxisCicle * math.sin(angle * math.pi /1800))
            
            if radiusChangeFlag:
                radiusCounterCircle = 10+offset
                if offset < offsetMax:
                    offset = offset + offsetIncrementFactor
                else:
                    offset=0

            value = colors['{}'.format(key)]
            colorImage[xCenter+x1,yCenter+y1,0] = value[0]
            colorImage[xCenter+x1,yCenter+y1,1] = value[1]
            colorImage[xCenter+x1,yCenter+y1,2] = value[2]
            for j in range(0,3600,1):                
                xxCenter = xCenter + x1
                yyCenter = yCenter + y1

                aangle = j
                xx1 = int(heightForCounterEllipse * radiusCounterCircle * math.cos(aangle * math.pi /1800))
                yy1 = int(widthForCounterEllipse * radiusCounterCircle * math.sin(aangle * math.pi /1800))

                # color pixel
                value = colors['{}'.format(key)]
                colorImage[xxCenter+xx1,yyCenter+yy1,0] = value[0]
                colorImage[xxCenter+xx1,yyCenter+yy1,1] = value[1]
                colorImage[xxCenter+xx1,yyCenter+yy1,2] = value[2]
        

        self.colorImage = colorImage

    def cycloidDrawingSingleEllipseWithRotaion(self,center=[500,500],radius=250,xAngle=1.2,yAngle=0.5,alpha=0):
        """
        Plain Ellipse drawing on canvas with appropriate angle,
        radius, and roate angle.

        Args:
            center ([int,int]) : center of the ellipse (x,y) pixel location.
            radius (int) : Radius for the ellipse.
            xAngle (float) : Combines with radius to give width of the ellipse.
            yAngle (float) : Combines wiht radius to give height of the ellipse.
            alpha (int) : Degree of roation given the ellipse from the center.

        """
        self.log.debug("cycloidDrawingEllipse")
        colorImage = self.blank_image
        colors = constants.COLORS_PANTONE_COOL
        xCenter = center[0]
        yCenter = center[1]
        r = radius
        key = random.randint(0, 4)
        key = 1
        for i in range(0,36000,10):
            angle = i/10
            xO = int(xAngle * r * math.cos(angle * math.pi /1080))
            yO = int(yAngle * r * math.sin(angle * math.pi /1080)) 
            
            if alpha is not 0:
                x1 = int(xO * math.cos(alpha*math.pi /360) - yO * math.sin(alpha*math.pi /360))
                y1 = int(xO * math.sin(alpha*math.pi /360) + yO * math.cos(alpha*math.pi /360))
            else:
                x1=xO
                y1=yO

            # color pixel
            value = colors['{}'.format(key)]
            colorImage[xCenter+x1,yCenter+y1,0] = value[0]
            colorImage[xCenter+x1,yCenter+y1,1] = value[1]
            colorImage[xCenter+x1,yCenter+y1,2] = value[2]
        self.colorImage = colorImage


    def cycloidDrawing(self,intialRadius=100,startCenter=[600,500],offsetStart=0,offsetEnd=200,offsetStep=4,color=None,portion=10):
        '''
        initialRadius   starting radius
        startCenter     starting center of the first circle
        offsetStart     
        '''
        self.log.debug("cycloidDrawing()")
        colorImage = self.blank_image
        colors = constants.COLORS_PANTONE_COOL

        for offset in range(offsetStart,offsetEnd,offsetStep):

            xCenter = startCenter[0] - (offset)
            yCenter = startCenter[1]
            r = intialRadius + offset
            if color is None:
                key = random.randint(0, len(colors)-1)
            else:
                key = color

            for i in range(0,3600,1):
                angle = i/portion
                x1 = int(r * math.cos(angle * math.pi /180))
                y1 = int(r * math.sin(angle * math.pi /180))

                # color pixel
                value = colors['{}'.format(key)]
                colorImage[xCenter+x1,yCenter+y1,0] = value[0]
                colorImage[xCenter+x1,yCenter+y1,1] = value[1]
                colorImage[xCenter+x1,yCenter+y1,2] = value[2]
        self.blank_image = colorImage 

    def cycloidDrawingCircleConeLowHighLow(self,noOfCircle=10,radiusRange=100,kKey=4):
        """
        creates a circle with center 500,500 and r = 250
        and makes cirlce, each point on this circle is 
        considered as the center for seriese of circles

        the key item is "portion" which draws some part of 
        the second cirlce whos center lays on the bigger cirlce 

        """
        self.log.debug(math.pi)
        colorImage = self.blank_image
        colors = constants.COLORS

        # outer circle center
        xCenter = 500
        yCenter = 500
        # outer circel radius 
        r = 250

        # porion of the smaller circle to show 
        portion = 10

        key = random.randint(0, 9)
        key = kKey
        self.log.debug("Key")
        self.log.debug(key)
        
        offset = 0
        up = True
        
        # degrees for bigger circle
        for i in range(0,3600,noOfCircle):
            angle = i/10
            x1 = int(r * math.cos(angle * math.pi /180))
            y1 = int(r * math.sin(angle * math.pi /180))
            
            rr = 1+offset
            
            if up:
                if offset < radiusRange:
                    offset = offset+1
                else:
                    up = False
            else:
                if offset > 0:
                    offset = offset-1
                else:
                    up = True
            # degrees for smaller cirlces on bigger circle
            for j in range(0,3600,1):
                
                xxCenter = xCenter + x1
                yyCenter = yCenter + y1

                aangle = j/portion
                xx1 = int(rr * math.cos(aangle * math.pi /180))
                yy1 = int(rr * math.sin(aangle * math.pi /180))

                # color pixel
                value = colors['{}'.format(key)]
                colorImage[xxCenter+xx1,yyCenter+yy1,0] = value[0]
                colorImage[xxCenter+xx1,yyCenter+yy1,1] = value[1]
                colorImage[xxCenter+xx1,yyCenter+yy1,2] = value[2]
        self.blank_image = colorImage

    def cycloidDrawingCircleIncreaseInCircle(self,noOfCircle=10,radiusRange=100,kKey=4):
        """
        creates a circle with center 500,500 and r = 250
        and makes cirlce, each point on this circle is 
        considered as the center for seriese of circles

        the key item is "noOfCircle" and "radiusRange" which 
        draws second cirlce which center lays on the bigger cirlce 
        radius and changes with the noOfCircle.

        """
        self.log.debug(math.pi)
        colorImage = self.blank_image
        colors = constants.COLORS

        # outer circle center
        xCenter = 500
        yCenter = 500
        # outer circel radius 
        r = 250

        # porion of the smaller circle to show 
        portion = 10

        key = random.randint(0, 9)
        key = kKey
        self.log.debug("Key")
        self.log.debug(key)
        
        offset = 0

        # degrees for bigger circle
        for i in range(0,3600,noOfCircle):
            angle = i/10
            x1 = int(r * math.cos(angle * math.pi /180))
            y1 = int(r * math.sin(angle * math.pi /180))
            
            rr = 10+offset
            if offset < radiusRange:
                offset = offset+1
            else:
                offset=0
            # degrees for smaller cirlces on bigger circle
            for j in range(0,3600,1):
                
                xxCenter = xCenter + x1
                yyCenter = yCenter + y1

                aangle = j/portion
                xx1 = int(rr * math.cos(aangle * math.pi /180))
                yy1 = int(rr * math.sin(aangle * math.pi /180))

                # color pixel
                value = colors['{}'.format(key)]
                colorImage[xxCenter+xx1,yyCenter+yy1,0] = value[0]
                colorImage[xxCenter+xx1,yyCenter+yy1,1] = value[1]
                colorImage[xxCenter+xx1,yyCenter+yy1,2] = value[2]
        self.blank_image = colorImage

    def cycloidDrawingSection(self):
        """
        creates a circle with center 500,500 and r = 250
        and makes cirlce on the above cirlce

        the key item is "portion" which draws some part of 
        the second cirlce whos center lays on the bigger cirlce 

        """
        self.log.debug(math.pi)
        colorImage = self.blank_image
        colors = constants.COLORS

        # outer circle center
        xCenter = 500
        yCenter = 500
        # outer circel radius 
        r = 250

        # porion of the smaller circle to show 
        portion = 40

        key = random.randint(0, 9)

        # degrees for bigger circle
        for i in range(0,3600,20):
            angle = i/10
            x1 = int(r * math.cos(angle * math.pi /180))
            y1 = int(r * math.sin(angle * math.pi /180))
            
            # degrees for smaller cirlces on bigger circle
            for j in range(0,3600,1):
                rr = 100
                xxCenter = xCenter + x1
                yyCenter = yCenter + y1

                aangle = j/portion
                xx1 = int(rr * math.cos(aangle * math.pi /180))
                yy1 = int(rr * math.sin(aangle * math.pi /180))

                # color pixel
                value = colors['{}'.format(key)]
                colorImage[xxCenter+xx1,yyCenter+yy1,0] = value[0]
                colorImage[xxCenter+xx1,yyCenter+yy1,1] = value[1]
                colorImage[xxCenter+xx1,yyCenter+yy1,2] = value[2]
        self.blank_image = colorImage        

    def drawCircleInCenter(self):
        self.log.debug(math.pi)
        colorImage = self.blank_image
        colors = constants.COLORS
        xCenter = 50
        yCenter = 50
        r = 25
        key = random.randint(0, 9)

        for i in range(0,3600,10):
            angle = i/10
            x1 = int(r * math.cos(angle * math.pi /180))
            y1 = int(r * math.sin(angle * math.pi /180))

            # color pixel
            value = colors['{}'.format(key)]
            colorImage[xCenter+x1,yCenter+y1,0] = value[0]
            colorImage[xCenter+x1,yCenter+y1,1] = value[1]
            colorImage[xCenter+x1,yCenter+y1,2] = value[2]
        self.colorImage = colorImage 

    def diagonalAttackPattern(self):
        """
        Refer data 'img/diagonalAttackPattern.png'
        """
        colorImage = self.blank_image
        colors = constants.COLORS
        for i in range(constants.HEIGHT):
            for j in range(constants.WIDTH):
                key = random.randint(0, 9)
                keyh = random.randint(6, 9)
                for k in range(key):
                    count = 0
                    for l in range(constants.WIDTH):
                        value = colors['{}'.format(key)]
                        colorImage[(i+k)*count,(j+k)*count,0] = value[0]
                        colorImage[(i+k)*count,(j+k)*count,1] = value[1]
                        colorImage[(i+k)*count,(j+k)*count,2] = value[2]
                        count+=4
                        if count > 10:
                            count=0
        num_rows, num_cols = colorImage.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 180, 1)
        colorImage = cv2.warpAffine(colorImage, rotation_matrix, (num_cols, num_rows))
        for i in range(constants.HEIGHT):
            for j in range(constants.WIDTH):
                key = random.randint(0, 9)
                keyh = random.randint(6, 9)
                for k in range(key):
                    count = 0
                    for l in range(constants.WIDTH):
                        value = colors['{}'.format(key)]
                        colorImage[(i+k)*count,(j+k)*count,0] = value[0]
                        colorImage[(i+k)*count,(j+k)*count,1] = value[1]
                        colorImage[(i+k)*count,(j+k)*count,2] = value[2]
                        count+=5
                        if count > 10:
                            count=0
        self.colorImage = colorImage        

    def shadowEffect(self):
        """
        Refer data 'img/shadowEffect.png'
        """
        colorImage = self.blank_image
        colors = constants.COLORS
        for i in range(constants.HEIGHT):
            for j in range(constants.WIDTH):
                key = random.randint(0, 9)
                keyh = random.randint(6, 9)
                for k in range(keyh):
                    for l in range(constants.WIDTH):
                        value = colors['{}'.format(key)]
                        colorImage[(i+k)*key,(j+l)*key,0] = value[0]
                        colorImage[(i+l)*key,(j+k)*key,1] = value[1]
                        colorImage[(i+k)*key,(j+l)*key,2] = value[2]
        self.colorImage = colorImage           

    def slantLinesPatterns(self):
        """
        Refer data 'img/slantLinesPatterns.png'
        """
        colorImage = self.blank_image
        colors = constants.COLORS
        for i in range(constants.HEIGHT):
            for j in range(constants.WIDTH):
                key = random.randint(0, 9)
                keyh = random.randint(6, 9)
                for k in range(keyh):
                    for l in range(constants.WIDTH):
                        value = colors['{}'.format(key)]
                        colorImage[(i+l)*keyh,(j+l)*keyh,0] = value[0]
                        colorImage[(i+l)*keyh,(j+l)*keyh,1] = value[1]
                        colorImage[(i+l)*keyh,(j+l)*keyh,2] = value[2]
        self.colorImage = colorImage           

    def mainPatternCreator(self):
        """
        10*10 by 10*10 image with pixel size 10*10
        """
        colorImage = self.blank_image
        colors = constants.COLORS
        for i in range(constants.HEIGHT):
            for j in range(constants.WIDTH):
                key = random.randint(0, 9)
                for k in range(constants.HEIGHT):
                    for l in range(constants.WIDTH):
                        value = colors['{}'.format(key)]
                        colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,0] = value[0]
                        colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,1] = value[1]
                        colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,2] = value[2]
        self.colorImage = colorImage           

    def randomEllips(self):
        """
        10*10 by 10*10 image with pixel size 10*10
        """
        colorImage = self.blank_image
        colors = constants.COLORS
        keyW = random.randint(0, 9)
        keyH = random.randint(0, 9)
        m_width = constants.WIDTH
        m_height = constants.HEIGHT
        for i in range(2,constants.HEIGHT-1):
            for j in range(2,constants.WIDTH-1):
                key = random.randint(0, 5)
                start = 0.01
                stop  = 0.1
                step  = 0.01
                precision = 0.001
                f = 1 / precision
                r = random.randrange(start*f, stop*f, step*f)/f
                for k in range(-1*m_height,m_height):
                    for l in range(-1*m_width,m_width):
                        
                        if((0.6*l*l*m_height*m_height+k*k*m_width*m_width+0.4*l*k*m_height*m_width)/r <= m_height*m_width*m_height*m_width):
                            value = colors['{}'.format(key)]
                            colorImage[k+i*m_height,l+j*m_width,0] = value[0]
                            colorImage[k+i*m_height,l+j*m_width,1] = value[1]
                            colorImage[k+i*m_height,l+j*m_width,2] = value[2]
        self.colorImage = colorImage 

    def crissCrossRain(self):
        """
        10*10 by 10*10 image with pixel size 10*10
        """
        colorImage = self.blank_image
        colors = constants.COLORS
        for i in range(2,constants.HEIGHT-1):
            for j in range(2,constants.WIDTH-1):
                key = random.randint(0, 5)
                keyW = random.randint(0, 9)
                keyH = random.randint(0, 9)
                for k in range(-1*constants.HEIGHT,constants.HEIGHT):
                    for l in range(-1*constants.WIDTH,constants.WIDTH):
                        if(l*l*constants.HEIGHT*constants.HEIGHT+k*k*constants.WIDTH*constants.WIDTH+2*random.randint(-1,1)*l*k*constants.WIDTH*constants.WIDTH <= constants.HEIGHT*constants.WIDTH*random.randint(1,5)*random.randint(1,5)):
                            value = colors['{}'.format(key)]
                            colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,0] = value[0]
                            colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,1] = value[1]
                            colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,2] = value[2]
        self.colorImage = colorImage

    def slantRain(self):
        """
        10*10 by 10*10 image with pixel size 10*10
        """
        colorImage = self.blank_image
        colors = constants.COLORS
        for i in range(2,constants.HEIGHT-1):
            for j in range(2,constants.WIDTH-1):
                key = random.randint(0, 5)
                keyW = random.randint(0, 9)
                keyH = random.randint(0, 9)
                for k in range(-1*constants.HEIGHT,constants.HEIGHT):
                    for l in range(-1*constants.WIDTH,constants.WIDTH):
                        if(l*l*constants.HEIGHT*constants.HEIGHT+k*k*constants.WIDTH*constants.WIDTH+2*l*k*constants.WIDTH*constants.WIDTH <= constants.HEIGHT*constants.WIDTH*random.randint(1,5)*random.randint(1,5)):
                            value = colors['{}'.format(key)]
                            colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,0] = value[0]
                            colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,1] = value[1]
                            colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,2] = value[2]
        self.colorImage = colorImage 

    def bluryPolkaDots(self):
        """
        10*10 by 10*10 image with pixel size 10*10
        """
        colorImage = self.blank_image
        colors = constants.COLORS
        for i in range(2,constants.HEIGHT-1):
            for j in range(2,constants.WIDTH-1):
                key = random.randint(0, 5)
                keyW = random.randint(0, 9)
                keyH = random.randint(0, 9)
                for k in range(-1*constants.HEIGHT,constants.HEIGHT):
                    for l in range(-1*constants.WIDTH,constants.WIDTH):
                        if(l*l*constants.HEIGHT*constants.HEIGHT+k*k*constants.WIDTH*constants.WIDTH <= constants.HEIGHT*constants.WIDTH*random.randint(0,5)*random.randint(0,15)):
                            value = colors['{}'.format(key)]
                            colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,0] = value[0]
                            colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,1] = value[1]
                            colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,2] = value[2]
        self.colorImage = colorImage            

    def circlesInBigSquare(self):
        """
        10*10 by 10*10 image with pixel size 10*10
        """
        colorImage = self.blank_image
        colors = constants.COLORS
        for i in range(2,constants.HEIGHT-1):
            for j in range(2,constants.WIDTH-1):
                key = random.randint(0, 9)
                keyW = random.randint(0, 9)
                keyH = random.randint(0, 9)

                for k in range(-1*constants.HEIGHT,constants.HEIGHT):
                    for l in range(-1*constants.WIDTH,constants.WIDTH):
                        if(l*l*constants.HEIGHT*constants.HEIGHT+k*k*constants.WIDTH*constants.WIDTH <= constants.HEIGHT*constants.HEIGHT*constants.WIDTH*constants.WIDTH):
                            value = colors['{}'.format(key)]
                            colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,0] = value[0]
                            colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,1] = value[1]
                            colorImage[k+i*constants.HEIGHT,l+j*constants.WIDTH,2] = value[2]
        self.colorImage = colorImage           

    def fourierPattern(self):
        """
        Refer data 'img/fourierPattern.png'
        """
        colorImage = self.blank_image
        colors = constants.COLORS
        for i in range(constants.HEIGHT):
            for j in range(constants.WIDTH):
                key = random.randint(0, 9)
                for k in range(constants.HEIGHT):
                    for l in range(constants.WIDTH):
                        value = colors['{}'.format(key)]
                        colorImage[i*k,j*l,0] = value[0]
                        colorImage[i*k,j*l,1] = value[1]
                        colorImage[i*k,j*l,2] = value[2]
        self.colorImage = colorImage           

    # individual sequence and objects

    def drawCircle(self,startDrawDegree,endDrawDegree,lineQuality,stepDraw,centerX,centerY,radius,colors,colorKey,portion):
        colorImage = self.blank_image
        h = len(colorImage)
        w = len(colorImage[0])

        for j in np.arange(startDrawDegree,endDrawDegree*lineQuality,stepDraw):
            angle = j/portion
            xx1 = radius * math.cos(angle * math.pi /180)
            yy1 = radius * math.sin(angle * math.pi /180)

            # color pixel
            value = colors['{}'.format(colorKey)]

            if centerX+xx1>h-1 or centerX+xx1<0 :
                continue
            if centerY+yy1>w-1 or centerY+yy1<0 :
                continue

            colorImage[int(centerX+xx1),int(centerY+yy1),0] = value[0]
            colorImage[int(centerX+xx1),int(centerY+yy1),1] = value[1]
            colorImage[int(centerX+xx1),int(centerY+yy1),2] = value[2]
        self.blank_image = colorImage

    def getLinePoints(self,x0,y0,x1,y1):
        """
        Get list of points between given points
        the function returns as yield
        """
        dx = x1-x0
        dy = y1-y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx>dy:
            xx,xy,yx,yy = xsign,0,0,ysign
        else:
            dx,dy=dy,dx
            xx,xy,yx,yy = 0,ysign,xsign,0

        D = 2*dy-dx
        y = 0

        for x in range(dx+1):
            yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
            if D >= 0:
                y += 1
                D -= 2*dx
            D += 2*dy

    def drawLine(self,x0,y0,x1,y1,colors,colorKey,lineThickness=1):
        """
        Thickness must be odd number to make the line evenly distributed
        """

        colorImage = self.blank_image
        if(self.h <= 0):
            return
        if(self.w <= 0):
            return

        # color pixel
        value = colors['{}'.format(colorKey)]

        if(self.h<=x0 or self.h<=x1 or 0>x0 or 0>x1):
            return
        if(self.w<=y0 or self.w<=y1 or 0>y0 or 0>y1):
            return


        for point in self.getLinePoints(x0,y0,x1,y1):

            
            x = point[0]
            y = point[1]

            colorImage[x,y,0] = value[0]
            colorImage[x,y,1] = value[1]
            colorImage[x,y,2] = value[2]

            # if lineThickness<=1:
            #     continue
            # for thickness in range((lineThickness-1)/2):

            #     if(self.h<=x-thickness or 0>x-thickness):
            #         continue
            #     if(self.w<=y-thickness or 0>y-thickness):
            #         continue

            #     colorImage[x-thickness,y-thickness,0] = value[0]
            #     colorImage[x-thickness,y-thickness,1] = value[1]
            #     colorImage[x-thickness,y-thickness,2] = value[2]

            #     if(self.h<=x+thickness or 0>x+thickness):
            #         continue
            #     if(self.w<=y+thickness or 0>y+thickness):
            #         continue

            #     colorImage[x+thickness,y+thickness,0] = value[0]
            #     colorImage[x+thickness,y+thickness,1] = value[1]
            #     colorImage[x+thickness,y+thickness,2] = value[2]
        self.blank_image = colorImage

    def drawSequenceCircle(self,x0,y0,x1,y1,frequencyCenters,radius,colors,colorKey,portion):
        """
        x0,y0,x1,y1 =  startX,startY,endX,endY
        """
        colorImage = self.blank_image
        if(self.h <= 0):
            return
        if(self.w <= 0):
            return

        # color pixel
        value = colors['{}'.format(colorKey)]

        steps = frequencyCenters
        for point in self.getLinePoints(x0,y0,x1,y1):

            if steps != frequencyCenters:
                steps+=1
                continue
            else:
                steps = 0

            x = point[0]
            y = point[1]

            self.drawCircle(
                startDrawDegree=0,
                endDrawDegree=360,
                lineQuality=1,
                stepDraw=0.5,
                centerX=point[0],
                centerY=point[1],
                radius=radius,
                colors=colors,
                colorKey=colorKey,
                portion=portion)