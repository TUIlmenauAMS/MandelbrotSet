#Apfemaennchen programm, more precisely: mandelbrot set.
#with zoom in with mouse 
#Gerald Schuller, February 2021

import numpy as np
#import cv2
#import matplotlib.pyplot as plt
import pygame

print("Erzeugt ein Bild vom Apfelmaennchen (Mandelbrot set) \n");

Nx=768; #horizontal pixels
Ny=768; #vertical pixels
xmin=-1.7; #image range of real part
#xmax=1.3;
ymin=-1.5; #image range or imaginary part
ymax=1.5;
#ymax=ymin+(xmax-xmin)*Ny/Nx #correct aspect ratio
xmax= xmin+ (ymax-ymin)*Nx/Ny #correct aspect ratio
limit=100; #iterations limit

newdraw=True #Flag if a new drawing should be made
screen = pygame.display.set_mode((Nx,Ny))
#screen2 = pygame.display.set_mode((Nx,Ny))
#screen2 = pygame.Surface((Nx,Ny))
#screen2.set_alpha(0)


#pygame.display.set_caption('Mandelbrot Set')
   
def draw_apfelmaennchen(screen, xmin,xmax,ymin,ymax,Nx,Ny,limit):
#computes and draws the Apfelmaennchen
   print("coordinates: xmin=", xmin, "xmax=", xmax, "ymin=", -ymin, "ymax=", -ymax)
   pygame.display.set_caption('Mandelbrot Set, center: x: '+str((xmax+xmin)/2)+', y: '+ str(-(ymax+ymin)/2)+', width: '+str(xmax-xmin))
   image=np.ones((Nx,Ny,3))*0
   [ix,iy,c]=image.shape
   pygame.init()  # Initializes pygame
   #Open graphics window:
   screen = pygame.display.set_mode((Nx,Ny))
   screen.fill((10, 100,100)) #background color
   #print(c)
   dx=(xmax-xmin)/Nx;
   dy=(ymax-ymin)/Ny;
   for x in range(Nx):
       for y in range(Ny):
          #set starting point in complex domain between -2 and 2:
          re=xmin+x*dx; #real part of starting point of iteration
          im=ymax-y*dy; #imaginary part of starting point of iteration
          c=re + 1j*im  #complex valued starting point

          #start iteration:
          z=0;
          it=0

          while (it< limit) and abs(z)<4:
             it=it+1
             z=z*z+c
          
          ma=it/limit;
          #print("ma=", ma)
          image[x,y,0]=ma;
          image[x,y,1]=np.abs(1-2*ma)
          image[x,y,2]=np.abs(1-ma)
          screen.set_at((x,Ny-1-y),255*image[x,y,:]) #pygame starts with y=0 at the top
          
       pygame.display.flip()
   return image 

if __name__ == '__main__':
   mousedown=False
   stop=False
   while stop==False:
     if newdraw==True:
        image= draw_apfelmaennchen(screen,xmin,xmax,ymin,ymax,Nx,Ny,limit) #draws a new Apfelmaennchen
        imagesurf=pygame.surfarray.make_surface(255*image[:,::-1,:]) #vertically flip, scaling
     newdraw=False
     ev = pygame.event.get()
     for event in ev:
       # handle MOUSEBUTTONDOWN
       if event.type == pygame.MOUSEBUTTONDOWN:
          posstart = pygame.mouse.get_pos()
          xmin_n = xmin + posstart[0]/Nx*(xmax-xmin)
          ymin_n = ymin + posstart[1]/Ny*(ymax-ymin)
          #print("pos=", pos, "new xmin=", xmin_n, "new ymin=", ymin_n)
          mousedown=True
       if mousedown==True:  #draw rectange:
          #print("Draw rectangle")
          pos = pygame.mouse.get_pos()
          #screen2.fill((0, 0, 0)) #background color
          #screen.blit(screen2, (0,0))
          screen.blit(imagesurf,(0,0))
          pygame.draw.rect(screen, (255, 0, 0), (posstart[0], posstart[1], (pos[0]-posstart[0]), (pos[1]-posstart[1])), 1)
          pygame.display.flip()
       # handle MOUSEBUTTONUP
       if event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          xmax_n = xmin + pos[0]/Nx*(xmax-xmin)
          ymax_n = ymin + pos[1]/Ny*(ymax-ymin)
          #print("pos[0]/Nx*(xmax-xmin)=", pos[0]/Nx*(xmax-xmin))
          #print("pos=", pos, "new xmax=", xmax_n, "new ymax=", ymax_n)
          xmin=xmin_n; xmax=xmax_n;
          ymin=ymin_n; ymax=ymin+ (xmax-xmin)*Ny/Nx #ymax_n; #image with constant ratio
          mousedown=False
          newdraw=True
       if event.type == pygame.K_q: #stops when key 'q' is pressed
                stop = True
       if event.type == pygame.QUIT: #stops when cross on window is clicked
                stop = True
       pygame.time.wait(10)
   """ 
       cv2.imshow('Apfelmaennchen',image)
       cv2.waitKey(1)
   while cv2.waitKey(1) & 0xFF != ord('q'):
      {}

   plt.imshow(image, aspect='equal')
   plt.show()
   """           


