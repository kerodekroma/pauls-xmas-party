# HOW TO RUN THIS SCRIPT IN TERMINAL:
# python -m snippets.button.py

# importing the proper dependencies
import pygame
import sys

from toolbox import colors, font, singl_button

PY_SINGLE_BUTTON_Events = singl_button.PY_SINGLE_BUTTON_Events

# Initializing Pygame
pygame.init()

palette = colors.PALETTE

# Defining the dimentions for our screen
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# current_key to print the current key pressed
current_key = ''
box_color = palette[1]

# The screen is almost ready, this is just the definition
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Font
pixel_font = font.pixel_font()

#single button square and circle setup
singl_btn_square = singl_button.SinglSquareButton((50,50), {'bg_color': palette[5], "text":"DEMO"})
singl_btn_circle = singl_button.SinglCircularButton((WINDOW_WIDTH/2,50), {'bg_color': palette[5]})

# Adding our awesone caption to show in the top of our fresh screen
pygame.display.set_caption("singl button")

# Flag to run our loop, it's optional in this example but useful to get used too
is_running = True
while is_running:
    # In this for loop is crazy! because its always listening which event is triggering
    for event in pygame.event.get():
        # And once is equal when a user closes the window
        # it will close the current window in execution 
        if event.type == pygame.QUIT:
            is_running = False
            pygame.quit()
            sys.exit()
        
        singl_btn_square.listen_events(event)
        singl_btn_circle.listen_events(event)

	# This is the magic sentence where our screen finally renders our DEMO_BG_COLOR, yay!
    screen.fill(palette[0])

    # check if singl_btn_square has clicked
    if singl_btn_square.current_event == PY_SINGLE_BUTTON_Events.PRESSED:
        singl_btn_square.options['bg_color'] = palette[4]

    if singl_btn_square.current_event == PY_SINGLE_BUTTON_Events.RELEASED:
        singl_btn_square.options['bg_color'] = palette[5]

    if singl_btn_circle.current_event == PY_SINGLE_BUTTON_Events.PRESSED:
        singl_btn_circle.options['bg_color'] = palette[6]

    if singl_btn_circle.current_event == PY_SINGLE_BUTTON_Events.RELEASED:
        singl_btn_circle.options['bg_color'] = palette[7]
        
    # rendering the buttons
    singl_btn_square.render(screen)
    singl_btn_circle.render(screen)

    # text to debug
    text_surface = pixel_font.render(f"has pressed?: {singl_btn_circle.current_event} ", True, palette[2])
    text_rect = text_surface.get_rect(topleft=(200, 350))
    screen.blit(text_surface, text_rect)

	# This method refreshes all the screen, is part of a good practice keep it here
    pygame.display.flip()
