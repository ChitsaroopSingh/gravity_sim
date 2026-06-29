import pygame
from ui.button import Button

class Panel:

    def __init__(self, width=280):

        self.width = width

        self.background = (20, 20, 30)
        self.border = (120, 120, 120)
        
        self.title_font = pygame.font.SysFont("Segoe UI", 22, bold=True)
        self.heading_font = pygame.font.SysFont("Segoe UI", 28, bold=True)
        self.text_font = pygame.font.SysFont("Segoe UI", 16)      
        self.preset_buttons = []
        self.action_buttons = []


        labels = [
            "Random",
            "Sun-Earth",
            "Earth-Moon",
            "Binary Stars",
            "Figure-8",
            "Infinity",
            "Solar System"
        ]

        for label in labels:
            self.preset_buttons.append(Button(label,0,0,0,26))

        action_labels = [
            "Pause",
            "Reset Camera",
            "Clear Bodies"
        ]

        for label in action_labels:
            self.action_buttons.append(Button(label,0,0,0,26))

        
    def draw(self, screen, stats):

        panel_rect = pygame.Rect(screen.get_width() - self.width, 0,self.width,screen.get_height())
        panel_x = panel_rect.left
        button_x = panel_x + 12
        button_width = self.width - 24


        pygame.draw.rect(screen, self.background, panel_rect)

        # Left border
        pygame.draw.line(screen,self.border,(panel_rect.left, 0),(panel_rect.left, screen.get_height()),2)

        # Title
        title = self.title_font.render("Gravity Simulator",True,"white")

        screen.blit(title, (panel_rect.left + 20,20))

        y = 70

        heading = self.text_font.render("Simulation", True, (255,255,120))
        
        # Divider
        pygame.draw.line(screen,(80, 80, 80),(panel_rect.left + 15, 60),(panel_rect.right - 15, 60),2)

        screen.blit(heading,(panel_rect.left+20, y))
        y+=28

        for key, value in stats.items():

            text = self.text_font.render(
                f"{key}: {value}",
                True,
                (220, 220, 220)
            )

            screen.blit(text, (panel_rect.left + 30, y))

            y += 24

        y+=10

        pygame.draw.line(screen,(70,70,70),(panel_rect.left+15,y),(panel_rect.right-15,y),2)

        y+=20

        #presets

        heading=self.text_font.render("Presets",True,(255,255,120))

        screen.blit(heading,(panel_rect.left+20,y))
        y+=40


        ###wip
        for button in self.preset_buttons:

            button.rect.x = button_x
            button.rect.y = y
            button.rect.width = button_width
            button.rect.height = 30

            button.draw(screen)

            y += 32
        

        pygame.draw.line(screen,(70,70,70),(panel_rect.left+15,y),(panel_rect.right-15,y),2)

        y += 20

        # actions

        heading = self.text_font.render("Actions",True,(255,255,120))

        screen.blit(heading,(panel_rect.left+20,y))

        y+=40

        for button in self.action_buttons:

            button.rect.x = button_x
            button.rect.y = y
            button.rect.width = button_width
            button.rect.height = 30

            button.draw(screen)

            y += 32

        

    def handle_event(self,event):
        for button in self.preset_buttons:
            if button.is_clicked(event):
                return button.text
        for button in self.action_buttons:
            if button.is_clicked(event):
                return button.text
        return None