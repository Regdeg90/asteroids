import pygame
from shot import Shot
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()
    shot = pygame.sprite.Group()
    Shot.containers =(shot, updatable, drawable)
    Asteroid.containers = (asteroid, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    # asteroid = Asteroid(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 5)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for u in updatable:
            u.update(dt)

        for a in asteroid:
            if a.is_collision(player):
                print("Game over!")
                return
            for s in shot:
                if s.is_collision(a):
                    a.split()
                    s.kill()

        screen.fill("black")

        for d in drawable:
            d.draw(screen=screen)

        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        



if __name__ == "__main__":
    main()