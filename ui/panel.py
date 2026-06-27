import pygame


class Panel:

    def __init__(self, width=300):

        self.width = width

        self.background = (20, 20, 30)
        self.border = (120, 120, 120)

    def draw(self, screen):

        panel_rect = pygame.Rect(screen.get_width() - self.width, 0,self.width,screen.get_height())

        pygame.draw.rect(screen, self.background, panel_rect)

        pygame.draw.line(screen,self.border,(panel_rect.left, 0),(panel_rect.left, screen.get_height()),2)