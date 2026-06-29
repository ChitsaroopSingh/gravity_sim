import pygame

class Button:
    def __init__(self,text,x,y,width,height):
        self.text = text
        self.rect = pygame.Rect(x,y,width,height)
        self.font = pygame.font.SysFont("Segoe UI", 18)

        self.bg = (45,45,60)
        self.hover = (70,70,100)
        self.text_color = (255,255,255)

    def draw(self,screen):
        mouse = pygame.mouse.get_pos()
        color = self.hover if self.rect.collidepoint(mouse) else self.bg

        pygame.draw.rect(screen,color,self.rect,border_radius=8)
        pygame.draw.rect(screen,(120,120,120),self.rect,2,border_radius=8)

        text = self.font.render(self.text,True,self.text_color)

        text_rect = text.get_rect(center=self.rect.center)

        screen.blit(text, text_rect)

    def is_clicked(self, event):

        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )