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
        # ip.paintWhite()

        #  add line of the frame
        # ip.drawLine(100,200,100,800,constants.COLORS_I_DEMAND,2)
        # ip.drawLine(100,800,900,800,constants.COLORS_I_DEMAND,2)
        # ip.drawLine(900,800,900,200,constants.COLORS_I_DEMAND,2)
        # ip.drawLine(900,200,100,200,constants.COLORS_I_DEMAND,2)

        ip.drawSequenceCircle(
            x0=46,
            y0=50,
            x1=46,
            y1=950,
            frequencyCenters=10,
            radius=44,
            colors=constants.COLORS_I_DEMAND,
            colorKey=0,
            portion=1
            )

        ip.drawSequenceCircle(
            x0=50,
            y0=50,
            x1=950,
            y1=50,
            frequencyCenters=10,
            radius=46,
            colors=constants.COLORS_I_DEMAND,
            colorKey=0,
            portion=1
            )

        ip.drawSequenceCircle(
            x0=50,
            y0=138,
            x1=950,
            y1=138,
            frequencyCenters=10,
            radius=46,
            colors=constants.COLORS_I_DEMAND,
            colorKey=0,
            portion=1
            )

        ip.drawSequenceCircle(
            x0=954,
            y0=50,
            x1=954,
            y1=950,
            frequencyCenters=10,
            radius=44,
            colors=constants.COLORS_I_DEMAND,
            colorKey=0,
            portion=1
            )


        ip.drawSequenceCircle(
            x0=950,
            y0=950,
            x1=50,
            y1=950,
            frequencyCenters=10,
            radius=46,
            colors=constants.COLORS_I_DEMAND,
            colorKey=0,
            portion=1
            )

        ip.drawSequenceCircle(
            x0=950,
            y0=862,
            x1=50,
            y1=862,
            frequencyCenters=10,
            radius=46,
            colors=constants.COLORS_I_DEMAND,
            colorKey=0,
            portion=1
            )

        #inner brown circle border
        ip.drawSequenceCircle(
            x0=120,
            y0=220,
            x1=880,
            y1=220,
            frequencyCenters=5,
            radius=20,
            colors=constants.COLORS_I_DEMAND,
            colorKey=0,
            portion=1
            )

        ip.drawSequenceCircle(
            x0=120,
            y0=780,
            x1=880,
            y1=780,
            frequencyCenters=5,
            radius=20,
            colors=constants.COLORS_I_DEMAND,
            colorKey=0,
            portion=1
            )
            
        ip.drawSequenceCircle(
            x0=120,
            y0=220,
            x1=120,
            y1=780,
            frequencyCenters=5,
            radius=20,
            colors=constants.COLORS_I_DEMAND,
            colorKey=0,
            portion=1
            )

        ip.drawSequenceCircle(
            x0=880,
            y0=220,
            x1=880,
            y1=780,
            frequencyCenters=5,
            radius=20,
            colors=constants.COLORS_I_DEMAND,
            colorKey=0,
            portion=1
            )

        # picture background
        ip.drawSequenceCircle(
            x0=200,
            y0=300,
            x1=200,
            y1=700,
            frequencyCenters=3,
            radius=50,
            colors=constants.MONALISA_BACKROUND,
            colorKey=0,
            portion=1
            )

        ip.drawSequenceCircle(
            x0=275,
            y0=300,
            x1=275,
            y1=700,
            frequencyCenters=3,
            radius=50,
            colors=constants.MONALISA_BACKROUND,
            colorKey=1,
            portion=1
            )    

        ip.drawSequenceCircle(
            x0=350,
            y0=300,
            x1=350,
            y1=700,
            frequencyCenters=3,
            radius=50,
            colors=constants.MONALISA_BACKROUND,
            colorKey=2,
            portion=1
            )  

        ip.drawSequenceCircle(
            x0=425,
            y0=300,
            x1=425,
            y1=700,
            frequencyCenters=3,
            radius=50,
            colors=constants.MONALISA_BACKROUND,
            colorKey=3,
            portion=1
            )  

        # background grass
        ip.drawSequenceCircle(
            x0=525,
            y0=300,
            x1=525,
            y1=700,
            frequencyCenters=3,
            radius=50,
            colors=constants.MONALISA_BACKROUND_GRASS,
            colorKey=0,
            portion=1
            )

        ip.drawSequenceCircle(
            x0=610,
            y0=300,
            x1=610,
            y1=700,
            frequencyCenters=3,
            radius=50,
            colors=constants.MONALISA_BACKROUND_GRASS,
            colorKey=1,
            portion=1
            )    

        ip.drawSequenceCircle(
            x0=695,
            y0=300,
            x1=695,
            y1=700,
            frequencyCenters=3,
            radius=50,
            colors=constants.MONALISA_BACKROUND_GRASS,
            colorKey=2,
            portion=1
            )  

        ip.drawSequenceCircle(
            x0=785,
            y0=310,
            x1=785,
            y1=690,
            frequencyCenters=3,
            radius=60,
            colors=constants.MONALISA_BACKROUND_GRASS,
            colorKey=3,
            portion=1
            )  

        # monalisa body
        ip.drawSequenceCircle(
            x0=340,
            y0=515,
            x1=755,
            y1=515,
            frequencyCenters=1,
            radius=90,
            colors=constants.MONALISA_BODY,
            colorKey=0,
            portion=1
            )  

        # Main body left inner cirle from face
        ip.drawSequenceCircle(
            x0=346,
            y0=570,
            x1=500,
            y1=590,
            frequencyCenters=10,
            radius=45,
            colors=constants.MONALISA_BODY,
            colorKey=0,
            portion=1
            )      

        # main body right inner circle from face
        ip.drawSequenceCircle(
            x0=350,
            y0=460,
            x1=500,
            y1=445,
            frequencyCenters=10,
            radius=45,
            colors=constants.MONALISA_BODY,
            colorKey=0,
            portion=1
            )       
        
        #shoulder white left
        ip.drawSequenceCircle(
            x0=570,
            y0=405,
            x1=765,
            y1=405,
            frequencyCenters=1,
            radius=80,
            colors=constants.MONALISA_BODY,
            colorKey=0,
            portion=1
            )     

        #shoulder white right
        ip.drawSequenceCircle(
            x0=570,
            y0=595,
            x1=765,
            y1=595,
            frequencyCenters=1,
            radius=80,
            colors=constants.MONALISA_BODY,
            colorKey=0,
            portion=1
            )     

        #shoulder white left
        ip.drawSequenceCircle(
            x0=710,
            y0=330,
            x1=795,
            y1=330,
            frequencyCenters=1,
            radius=50,
            colors=constants.MONALISA_BODY,
            colorKey=0,
            portion=1
            )       

        #shoulder white left
        ip.drawSequenceCircle(
            x0=710,
            y0=640,
            x1=795,
            y1=640,
            frequencyCenters=1,
            radius=50,
            colors=constants.MONALISA_BODY,
            colorKey=0,
            portion=1
            )           

        #Face 
        ip.drawSequenceCircle(
            x0=340,
            y0=520,
            x1=475,
            y1=520,
            frequencyCenters=1,
            radius=50,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=1,
            portion=1
            )
        ip.drawSequenceCircle(
            x0=339,
            y0=521,
            x1=474,
            y1=521,
            frequencyCenters=1,
            radius=50,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=1,
            portion=1
            )      
        
        #Face 
        ip.drawSequenceCircle(
            x0=335,
            y0=490,
            x1=420,
            y1=490,
            frequencyCenters=1,
            radius=60,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=0,
            portion=1
            ) 
        
        ip.drawSequenceCircle(
            x0=336,
            y0=491,
            x1=419,
            y1=491,
            frequencyCenters=1,
            radius=60,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=0,
            portion=1
            )
        ip.drawSequenceCircle(
            x0=335,
            y0=490,
            x1=430,
            y1=490,
            frequencyCenters=1,
            radius=40,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=0,
            portion=1
            ) 
        
        ip.drawSequenceCircle(
            x0=336,
            y0=491,
            x1=429,
            y1=491,
            frequencyCenters=1,
            radius=40,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=0,
            portion=1
            )  

        #face features
        ip.drawSequenceCircle(
            x0=350,
            y0=550,
            x1=350,
            y1=495,
            frequencyCenters=1,
            radius=7,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=1,
            portion=1
            )
        ip.drawSequenceCircle(
            x0=350,
            y0=551,
            x1=350,
            y1=496,
            frequencyCenters=1,
            radius=7,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=1,
            portion=1
            )
        ip.drawSequenceCircle(
            x0=350,
            y0=495,
            x1=415,
            y1=495,
            frequencyCenters=1,
            radius=7,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=1,
            portion=1
            )
        ip.drawSequenceCircle(
            x0=351,
            y0=496,
            x1=416,
            y1=496,
            frequencyCenters=1,
            radius=7,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=1,
            portion=1
            )

        #chest
        ip.drawSequenceCircle(
            x0=555,
            y0=551,
            x1=555,
            y1=451,
            frequencyCenters=1,
            radius=50,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=1,
            portion=1
            )          
        ip.drawSequenceCircle(
            x0=556,
            y0=550,
            x1=556,
            y1=450,
            frequencyCenters=1,
            radius=50,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=1,
            portion=1
            )          
       
        #cloth on shoulder
        ip.drawSequenceCircle(
            x0=570,
            y0=595,
            x1=765,
            y1=430,
            frequencyCenters=1,
            radius=80,
            colors=constants.MONALISA_BODY,
            colorKey=0,
            portion=1
            ) 
        ip.drawSequenceCircle(
            x0=571,
            y0=596,
            x1=766,
            y1=431,
            frequencyCenters=1,
            radius=80,
            colors=constants.MONALISA_BODY,
            colorKey=0,
            portion=1
            ) 
        ip.drawSequenceCircle(
            x0=531,
            y0=401,
            x1=766,
            y1=401,
            frequencyCenters=1,
            radius=40,
            colors=constants.MONALISA_BODY,
            colorKey=0,
            portion=1
            ) 
        

        #hands right
        ip.drawSequenceCircle(
            x0=765,
            y0=566,
            x1=765,
            y1=421,
            frequencyCenters=1,
            radius=30,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=1,
            portion=1
            )          
        ip.drawSequenceCircle(
            x0=766,
            y0=565,
            x1=766,
            y1=420,
            frequencyCenters=1,
            radius=30,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=1,
            portion=1
            )   
        ip.drawSequenceCircle(
            x0=785,
            y0=406,
            x1=765,
            y1=421,
            frequencyCenters=1,
            radius=30,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=1,
            portion=1
            )          
        ip.drawSequenceCircle(
            x0=786,
            y0=406,
            x1=766,
            y1=420,
            frequencyCenters=1,
            radius=30,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=1,
            portion=1
            )             

        #hands left
        ip.drawSequenceCircle(
            x0=740,
            y0=466,
            x1=715,
            y1=321,
            frequencyCenters=1,
            radius=30,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=0,
            portion=1
            )          
        ip.drawSequenceCircle(
            x0=741,
            y0=465,
            x1=716,
            y1=320,
            frequencyCenters=1,
            radius=30,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=0,
            portion=1
            )    
        #wrist
        ip.drawSequenceCircle(
            x0=720,
            y0=481,
            x1=770,
            y1=531,
            frequencyCenters=1,
            radius=8,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=0,
            portion=1
            )          
        ip.drawSequenceCircle(
            x0=721,
            y0=480,
            x1=771,
            y1=530,
            frequencyCenters=1,
            radius=8,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=0,
            portion=1
            )    
        ip.drawSequenceCircle(
            x0=720,
            y0=451,
            x1=765,
            y1=491,
            frequencyCenters=1,
            radius=15,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=0,
            portion=1
            )          
        ip.drawSequenceCircle(
            x0=721,
            y0=450,
            x1=765,
            y1=490,
            frequencyCenters=1,
            radius=15,
            colors=constants.MONALISA_BODY_SKIN,
            colorKey=0,
            portion=1
            )    

    def Save(self, name="MonaLisa"):
        self.ip.saveImage(name)   

