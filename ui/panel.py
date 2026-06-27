import pygame


class Panel:

    def __init__(self, width=300):

        self.width = width

        self.background = (20, 20, 30)
        self.border = (120, 120, 120)
        
        self.title_font = pygame.font.SysFont(None, 34)
        self.text_font = pygame.font.SysFont(None, 28)       

    def draw(self, screen, stats):

        panel_rect = pygame.Rect(screen.get_width() - self.width, 0,self.width,screen.get_height())

        pygame.draw.rect(screen, self.background, panel_rect)

        # Left border
        pygame.draw.line(screen,self.border,(panel_rect.left, 0),(panel_rect.left, screen.get_height()),2)

        # Title
        title = self.title_font.render("Gravity Simulator",True,"white")

        screen.blit(title, (panel_rect.left + 20, 20))

        # Divider
        pygame.draw.line(screen,(80, 80, 80),(panel_rect.left + 15, 60),(panel_rect.right - 15, 60),2)

        # Stats
        y = 80

        for key, value in stats.items():

            text = self.text_font.render(
                f"{key}: {value}",
                True,
                (220, 220, 220)
            )

            screen.blit(text, (panel_rect.left + 20, y))

            y += 30