# -*- coding: utf-8 -*-
"""
Spyder Editor
Author Isaac Nape
"""

# packages 
#from PIL import Image
#import pyglet
import numpy as np 
import matplotlib.pyplot as plt
import math
#import seaborn as sb
#packages 


class MySimpleHolo:
    def __init__(self, HDimension, VDimension, HResolution, VResoluton):
        x = np.linspace(-HDimension/2,VDimension/2 -1, HDimension)*HResolution;
        y = np.linspace(-HDimension/2,VDimension/2 -1, HDimension)*HResolution;
        self.X, self.Y = np.meshgrid(x, y);
        self.r = np.sqrt(self.X**2 + self.Y**2);
        self.phi = np.arctan2(self.Y, self.X);
        
    def GenHolo(self, Field, Xgrating, Ygrating ):
        phaseAngle =np.angle(Field); 
        amplitude = abs( Field );
        Holo = amplitude * np.mod( phaseAngle + self.X * Xgrating * 2*np.pi + self.Y * Ygrating * 2*np.pi, 2*np.pi);
        return Holo;

def LGmode(Base, ell, w):
    Phasesor = np.exp(-1j * Base.phi * ell );
    Amplitude =( (Base.r /w)* np.sqrt( 2 ))**(abs(ell)) * np.exp(-(Base.r / w)**2 );
    Norma = np.sqrt( 2 / (np.pi*(math.factorial(ell))) ); 
    Field = Norma*Phasesor*Amplitude;
    return  np.mod(np.angle(Phasesor), 2*np.pi), Field;



 # parameters for base   
H=600; 
V=600;
dx=8e-6;
dy=8e-6;
xgrating=(10*dx);
ygrating=(10*dy);
OAM = 10;
w=0.5e-3;

 # instantiation and holo calc  
Base = MySimpleHolo(H, V, dx, dy); # create grid object
ModeFunc =list(LGmode(Base, OAM, w));
hologram = Base.GenHolo(ModeFunc[1], 1/ xgrating, 1/ygrating); # generate hologram object
ModeFunc.append( hologram );

# plot 

fig , axlist = plt.subplots(nrows=1, ncols=len(ModeFunc))
fig.set_size_inches(18.5, 10.5)
plt.figure(figsize=(10, 10), dpi=100, facecolor='w')
titlelist= ['phase', 'Intensity', 'hologram'];
for i in range(len( axlist)-0):# #np.linspace( 0, len(axlist)-1, len(axlist) ):
    axlist[i].imshow(abs(ModeFunc[i]), interpolation='none')
    axlist[i].axis('off')
    axlist[i].set_title(titlelist[i])

plt.show()
#window = pyglet.window.Window()    
#im = Image.fromarray(A)
#image = pyglet.resource.image(im)    
#    @window.event
#def on_draw():
#    window.clear()
#    image.blit(0, 0)
#
#pyglet.app.run()


    
axlist[2].imshow(hologram, interpolation='none')  
axlist[2].set_title(titlelist[2])
axlist[2].axis('off')
plt.show()



