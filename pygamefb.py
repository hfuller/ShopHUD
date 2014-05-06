import os
import pygame
import time
import random
 
class pyscope :
  screen = None;

  def __init__(self):
    "Ininitializes a new pygame screen using the framebuffer"
    # Based on "Python GUI in Linux frame buffer"
    # http://www.karoltomala.com/blog/?p=679
    
    found = False
    
    #first try X    
    disp_no = os.getenv("DISPLAY")
    if disp_no:
      print "I'm running under X display = {0}".format(disp_no)
      found = True 
      try:
        pygame.display.init()
      except pygame.error:
        print 'X failed.'
        #continue
    else:
      print "Well, there's no X."
        

    # Check which frame buffer drivers are available
    # Start with fbcon since directfb hangs with composite output
    drivers = ['directfb', 'svgalib', 'fbcon']
    for driver in drivers:
      if not found: #only try this if we don't already have a dpy
        # Make sure that SDL_VIDEODRIVER is set
        print "Trying " + driver
        if not os.getenv('SDL_VIDEODRIVER'):
          os.putenv('SDL_VIDEODRIVER', driver)
        try:
          pygame.display.init()
        except pygame.error:
          print 'Driver: {0} failed.'.format(driver)
          continue
        found = True
        print "Using driver " + driver

        break

    if not found:
      raise Exception('No suitable video driver found!')

    
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    print "Output dpy size: %d x %d" % (size[0], size[1])
    self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    # Clear the screen to start
    self.screen.fill((0, 0, 0))
    # Initialise font support
    pygame.font.init()
    # Render the screen
    pygame.display.update()
    
    #hide mouse
    pygame.mouse.set_visible(False)
   
  def __del__(self):
    "Destructor to make sure pygame shuts down, etc."
   
  def test(self):
    # Fill the screen with red (255, 0, 0)
    red = (255, 0, 0)
    self.screen.fill(red)
    # Update the display
    pygame.display.update()
    
  def updateTime(self):
    font = pygame.font.Font(None,120)
    text = font.render("butts",1,(255,255,255))
    textpos = text.get_rect()
    screenrect = self.screen.get_rect()
    textpos.centerx = screenrect.centerx
    textpos.centery = screenrect.centery
    self.screen.blit(text,textpos)
    pygame.display.update()
    #pygame.display.flip()
 
# Create an instance of the PyScope class
scope = pyscope()
#scope.test()
scope.updateTime()
time.sleep(10)
