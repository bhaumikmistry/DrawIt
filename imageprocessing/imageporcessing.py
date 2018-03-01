
import sys
sys.path.insert(0,'../')

import logging
import cv2
import numpy as np
from config.constants import constants
import random

class imageprocessing:

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.log.debug('__init__()')

    def createImage(self):
        self.blank_image = np.zeros((constants.HEIGHT*constants.HEIGHT,constants.WIDTH*constants.WIDTH,constants.CHANNELRGB), np.uint8)

    def saveImage(self,name='m'):
        """
        saveImage for the current object, 
        default name is m.png
        arg :
        name -> string # name of the file without extension.
        """
        self.name = ""
        self.name = name
        cv2.imwrite('{}.png'.format(name),self.colorImage)    
        
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
