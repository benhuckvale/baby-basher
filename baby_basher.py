import pygame, sys, os, random
import pygame.mixer

__location__ = os.path.realpath(os.path.join(os.getcwd(),
                                os.path.dirname(__file__)))
sound_file = os.path.join(__location__, 'boop.wav')

screen_width=1280
screen_height=704

class colour:
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    darkBlue = (0, 0, 128)
    white = (255, 255, 255)
    black = (0, 0, 0)
    pink = (255, 200, 200)

    @staticmethod
    def random():
        return random.choice([colour.red, colour.green, colour.blue, colour.darkBlue, colour.white, colour.pink])

def make_coords_for_char(s):
   return {c: (x, y)
           for y, l in enumerate(s.split("\n"))
           for x, c in enumerate(l) }
         
keyboard_layout="""
1 2 3 4 5 6 7 8 9 0 - =
 q w e r t y u i o p [ ]
  a s d f g h j k l ; '
   z x c v b n m , . /
"""

coords_for_char=make_coords_for_char(keyboard_layout)
sx = screen_width / max([a[0] for a in coords_for_char.values()])
sy = screen_height / max([a[1] for a in coords_for_char.values()])

def fudge_coords(x, y):
    gx = x*sx
    gy = (y-1)*sy
    rx = random.normalvariate(0, 30.0)
    ry = random.normalvariate(0, 30.0)
    return gx+rx, gy+ry
    
pygame.init() 

screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption('Basher') 

pygame.mixer.init()
sound = pygame.mixer.Sound(sound_file)
 
def process_events(events):
   quit=False
   for event in events: 
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE:
              quit=True 
          else:
              try:
                  x, y = fudge_coords(*coords_for_char[event.unicode])
                  r=pygame.Rect(x, y, random.randint(30, 150), random.randint(30,150))
                  pygame.draw.rect(screen, colour.random(), r, 0)
                  sound.play()
              except KeyError:
                  pass
      if event.type == pygame.QUIT: 
          quit=True
   if quit:
       sys.exit(0) 

while True: 
   process_events(pygame.event.get())  
   pygame.display.flip() 
   pygame.time.wait(200)
