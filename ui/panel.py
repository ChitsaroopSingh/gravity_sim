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

        y = 70

        heading = self.text_font.render("Simulation", True, (255,255,120))
        
        # Divider
        pygame.draw.line(screen,(80, 80, 80),(panel_rect.left + 15, 60),(panel_rect.right - 15, 60),2)

        screen.blit(heading,(panel_rect.left+20, y))
        y+=35

        for key, value in stats.items():

            text = self.text_font.render(
                f"{key}: {value}",
                True,
                (220, 220, 220)
            )

            screen.blit(text, (panel_rect.left + 30, y))

            y += 28

        y+=15

        pygame.draw.line(screen,(70,70,70),(panel_rect.left+15,y),(panel_rect.right-15,y),2)

        y+=20

        #presets

        heading=self.text_font.render("Presets",True,(255,255,120))

        screen.blit(heading,(panel_rect.left+20,y))
        y+=40

        presets = [
        "Random System",
        "Sun - Earth",
        "Earth - Moon",
        "Binary Stars",
        "Figure-8 Orbit",
        "Infinity Orbit",
        "Solar System"
        ]

        for preset in presets:
            txt = self.text_font.render(preset,True,(170,220,255))

            screen.blit(txt, (panel_rect.left+30,y))
            y += 30

        y+=15

        pygame.draw.line(screen,(70,70,70),(panel_rect.left+15,y),(panel_rect.right-15,y),2)

        y += 20
