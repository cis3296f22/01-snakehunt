import pygame
import pygame.gfxdraw

buttons = pygame.sprite.Group()
screen = pygame.display.set_mode((600, 400))
class Button(pygame.sprite.Sprite):
    def __init__(self, position, text, size, colors="white on blue", borderc=(255,255,255), command=lambda: print("No command defined")):
        super().__init__()
        self.text = text
        self.command = command
        
        # colors
        self.colors = colors
        self.original_colors = colors
        self.fg, self.bg = self.colors.split(" on ")
        self.hover_colors = f"{self.bg} on {self.fg}"
        self.borderc = borderc 
        
        # font
        self.font = pygame.font.SysFont("Arial", size)
        self.render()
        self.x, self.y, self.w , self.h = self.text_render.get_rect()
        self.x, self.y = position
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.position = position
        self.pressed = 1
        
        buttons.add(self)

    def draw_button(self):
        # draws border of button, 4 lines around plus background
        # horizontal up
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y), (self.x + self.w , self.y), 5)
        pygame.draw.line(screen, (150, 150, 150), (self.x, self.y - 2), (self.x, self.y + self.h), 5)
        # horizontal down
        pygame.draw.line(screen, (50, 50, 50), (self.x, self.y + self.h), (self.x + self.w , self.y + self.h), 5)
        pygame.draw.line(screen, (50, 50, 50), (self.x + self.w , self.y + self.h), [self.x + self.w , self.y], 5)
        # background
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.w , self.h))  

    def hover(self):
        # checks if mouse over button, and change color if true
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.colors = self.hover_colors
        else:
            self.colors = self.original_colors
        self.render()

    def click(self):
        # checks if button clicked, and make call to action just once
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] and self.pressed == 1:
                print("Executing code for button '" + self.text + "'")
                self.command()
                self.pressed = 0
            if pygame.mouse.get_pressed() == (0,0,0):
                self.pressed = 1
                
    def render(self):
        self.text_render = self.font.render(self.text, 1, self.fg)
        self.image = self.text_render

    def update(self):
        self.fg, self.bg = self.colors.split(" on ")
        self.draw_button()
        self.hover()
        self.click()
