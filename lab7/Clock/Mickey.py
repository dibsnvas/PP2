import pygame
import datetime
import os

pygame.init()
done = False


window_width = 829
window_height = 836
game_display = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
print(os.getcwd())

bg = pygame.image.load(os.path.normpath('main1.png'))
hand_second = pygame.image.load(os.path.normpath('lefthand.png'))
hand_minute = pygame.image.load(os.path.normpath('righthand.png'))
rect = bg.get_rect(center=(415, 418))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    time = datetime.datetime.now()

    angle_second = -(time.second * 6)
    angle_minute = -(time.minute * 6)
                
    game_display.blit(bg, (0, 0))
    
    
    hand_minute_img = pygame.transform.rotate(hand_minute, angle_minute)
    hand_minute_rect = hand_minute_img.get_rect(center=rect.center)
    game_display.blit(hand_minute_img, hand_minute_rect.topleft)
    
    hand_second_img = pygame.transform.rotate(hand_second, angle_second)
    hand_second_rect = hand_second_img.get_rect(center=rect.center)
    game_display.blit(hand_second_img, hand_second_rect.topleft)
    
    
    pygame.display.flip()
    
pygame.quit()
