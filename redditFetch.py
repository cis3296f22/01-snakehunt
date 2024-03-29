import redditwarp.SYNC

def fetch_latest_temple_post():
    client = redditwarp.SYNC.Client()
    post = next(client.p.subreddit.pull.top('Temple', amount=1, time='hour'))
    return post.title, post.permalink

import pygame
import textwrap

def display_text(window, text, position, font_size=15, color=(255, 255, 255), max_width= 75):
    font = pygame.font.Font(None, font_size)
    words = text.split(' ')
    wrapped_text = textwrap.fill(text, width=max_width)
    
    y_offset = 0
    for line in wrapped_text.split('\n'):
        text_surface = font.render(line, True, color)
        window.blit(text_surface, (position[0], position[1] + y_offset))
        y_offset += font_size  # Increase the y offset for each line to avoid overlap



