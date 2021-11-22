import pygame
from sys import exit

pygame.init()

width=800
height=400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
#test_font = pygame.font.Font(None, 50)
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True

sw=100
sh=200
#test_surface = pygame.Surface((sw,sh))
#test_surface.fill('Red')
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('My game', False, (64,64,64))
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
        #    if player_rect.collidepoint(event.pos): print('collision')
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity  = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity  = -20
                    print('jump')

            if event.type == pygame.KEYUP:
                print('key up')
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800


    if game_active:
        # draw all our elements
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect,10)
        #pygame.draw.line(screen, 'Gold', (0,0),(width,height),10)
        #pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50,200,100,100))
        screen.blit(score_surf,score_rect)
        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = width
        screen.blit(snail_surf,snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        # collision
        if snail_rect.colliderect(player_rect):
            game_active = False

        # Player input
        #keys = pygame.key.get_pressed()
        #if keys[pygame.K_SPACE]:
        #    print('jump')

        #if player_rect.colliderect(snail_rect):
        #    print('collision')

        #mouse_pos = pygame.mouse.get_pos()
        #if player_rect.collidepoint(mouse_pos):
        #    print(pygame.mouse.get_pressed())
        # update everything
    else:
        screen.fill('Yellow')

    pygame.display.update()
    clock.tick(60)
