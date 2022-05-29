import sys
import pygame
def run_game():
 # Initialize game and create a screen object.
   pygame.init()
   screen = pygame.display.set_mode((1200, 800))
   pygame.display.set_caption("Dutt's Alien Invasion")
 # Start the main loop for the game.
   while True:
 # Watch for keyboard and mouse events.
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
       sys.exit()

 #hello
    pygame.display.set_caption("Alien Invasion")
 # Set the background color.
    bg_color = (900, 900, 900)
 # Start the main loop for the game.
    while True:
 # Watch for keyboard and mouse events.
 # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
 # Make the most recently drawn screen visible.
        pygame.display.flip()
     
 # Make the most recently drawn screen visible.
       pygame.display.flip()

  from settings import Settings
  from ship import Ship
  from settings import Settings
def run_game():
 # Initialize pygame, settings, and screen object.
  pygame.init()
ai_settings = Settings()
screen = pygame.display.set_mode(
   (ai_settings.screen_width, ai_settings.screen_height))
pygame.display.set_caption("Alien Invasion")
 # Start the main loop for the game.
while True:

 # Redraw the screen during each pass through the loop.
   screen.fill(ai_settings.bg_color)

 # Make the most recently drawn screen visible.
   pygame.display.flip()
  
   pygame.display.set_caption("Alien Invasion")
 # Make a ship.
   ship = Ship(screen)
 # Start the main loop for the game.
   while True:
 
 # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

 # Make the most recently drawn screen visible.
    pygame.display.flip()

run_game() 

