import pygame
pygame.init ()

#initial variable 
p = 0.07 #hằng trọng lực
score = 0 #initial score
bird_y = 0 #chaging bird fly
floor_x = 0 #moving floor
game_play = True

#font
game_font = pygame.font.Font(r'D:\Workspace_f8\python\pyGame\FileGame\04B_19.TTF', 40)

#score
def score_view(score):
    if game_play:
        score_f = game_font.render(f'Score : {int(score)}', True, (255, 255, 255))
        score_hcn = score_f.get_rect(center=(162, 50))
        screen.blit(score_f, score_hcn)
    else:
        score_f = game_font.render(f'Score : {int(score)}', True, (255, 255, 255))
        score_hcn = score_f.get_rect(center=(162, 50))
        screen.blit(score_f, score_hcn)

#titile, icon, background, floor, bird
pygame.display.set_caption("Flappy bird") 
icon = pygame.image.load(r'D:\Workspace_f8\python\pyGame\FileGame\assets\yellowbird-midflap.png')
bg = pygame.image.load(r'D:\Workspace_f8\python\pyGame\FileGame\assets\background-night.png') #background
floor = pygame.image.load(r'D:\Workspace_f8\python\pyGame\FileGame\assets\floor.png')
bird = pygame.image.load(r'D:\Workspace_f8\python\pyGame\FileGame\assets\yellowbird-midflap.png')

bg = pygame.transform.scale(bg, (324, 576)) 
floor = pygame.transform.scale(floor, (504, 168)) 

bird = pygame.transform.scale(bird, (51, 36)) 
bird_hcn = bird.get_rect(center=(80, 200))

pygame.display.set_icon(icon)

#cua so game
screen = pygame.display.set_mode((324, 576))

#game over screen
over = pygame.image.load(r'D:\Workspace_f8\python\pyGame\FileGame\assets\message.png')
over = pygame.transform.scale(over, (217, 315))
over_hcn = over.get_rect(center=(162, 250))
 
#check to stop playing
def check():
    if bird_hcn.bottom >= 420 or bird_hcn.top <= -50:
        return False
    else:
        return True

#on-screen
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_play: 
                bird_y -= 7
            elif event.key == pygame.K_SPACE and not game_play:
                game_play = True
                bird_y = 0
                bird_hcn.center = (80, 200)
                score = 0
    screen.blit(bg, (0, 0))
    floor_x -= 1
    screen.blit(floor, (floor_x, 408))
    screen.blit(floor, (floor_x + 324, 408))
    if floor_x == -324:
            floor_x = 0
    if game_play:
        screen.blit(bird, bird_hcn)
        bird_y += p
        bird_hcn.centery += bird_y
        score += 0.01
        score_view(score)
        game_play = check()
    else:
        screen.blit(over, over_hcn)
        score_view(score)
    pygame.display.update()
