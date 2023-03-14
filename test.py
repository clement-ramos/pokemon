import pygame, sys

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

#PYGAME
pygame.init()

# window parameter
#255, 143
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# clock parameter
clock = pygame.time.Clock() #clock normalize speed of exe in every computer(not impacted anymore by it calculation speed)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) #150 ms 

BackGround = Background('assets/background/battleground.png', [0,0])

#Main loop
def main():
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # display elements


        # Draw buttons 

        # timer and FPS
        pygame.display.update()
        clock.tick(60)

main()