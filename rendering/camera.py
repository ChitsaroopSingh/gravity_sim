class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.zoom = 1.0
    
    def world_to_screen(self, world_pos):
        screen_x = (world_pos[0] - self.x) * self.zoom
        screen_y = (world_pos[1] - self.y) * self.zoom

        return (screen_x,screen_y)
    
    def screen_to_world(self , screen_pos):
        world_x = self.x + screen_pos[0] / self.zoom
        world_y = self.y + screen_pos[1] / self.zoom

        return (world_x,world_y)
    
    