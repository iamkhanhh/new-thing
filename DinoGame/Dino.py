import pygame
pygame.mixer.pre_init()
pygame.init()
clock = pygame.time.Clock()

#screen, titile, icon
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Dinosour game')
icon_dino = pygame.image.load(r'D:\Workspace_f8\python\DinoGame\dino\assets\dinosaur.png')
pygame.display.set_icon(icon_dino) #set icon

#check collision
def collision():
    if dino_hcn.colliderect(tree_hcn):
        over_sound.play()
        return False
    return True

#font
game_font = pygame.font.Font(r'D:\Workspace_f8\python\DinoGame\dino\04B_19.TTF', 40)

#sounds
jump_sound = pygame.mixer.Sound(r'D:\Workspace_f8\python\DinoGame\dino\sound\tick.wav')
over_sound = pygame.mixer.Sound(r'D:\Workspace_f8\python\DinoGame\dino\sound\te.wav')

#background, dino, tree
bg = pygame.image.load(r'D:\Workspace_f8\python\DinoGame\dino\assets\background.jpg')
tree = pygame.image.load(r'D:\Workspace_f8\python\DinoGame\dino\assets\tree.png')
dino = pygame.image.load(r'D:\Workspace_f8\python\DinoGame\dino\assets\dinosaur.png')

#initial position
bg_x, bg_y = 0, 0
tree_x, tree_y = 530, 230
dino_x, dino_y = 50, 230
jump = False
gameplay = True
score = 0

#show score
def show_score(score):
    if gameplay:
        score_f = game_font.render(f'Score : {int(score)}', True, (0, 0, 0))
        score_hcn = score_f.get_rect(center=(300, 80))
        screen.blit(score_f, score_hcn)
    else:
        score_f = game_font.render(f'Score : {int(score)}', True, (0, 0, 0))
        score_hcn = score_f.get_rect(center=(300, 80))
        screen.blit(score_f, score_hcn)

#over screen
over = game_font.render('GAME OVER', True, (0, 0, 0))

#running
running = True
while running:
    #fps
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and gameplay:
                if dino_y == 230:
                    jump = True
                    jump_sound.play()
            elif event.key == pygame.K_SPACE and not gameplay:
                tree_x, tree_y = 530, 230
                dino_x, dino_y = 50, 230
                jump = False
                score = 0
                gameplay = True

    screen.blit(bg, (bg_x, bg_y))    
    screen.blit(bg, (bg_x + 600, bg_y))  
    tree_hcn = screen.blit(tree, (tree_x, tree_y))    
    dino_hcn = screen.blit(dino, (dino_x, dino_y))   
    if gameplay:
        bg_x -= 4
        if bg_x == -600:
            bg_x = 0  
        tree_x -= 4
        if tree_x <= -20:
            tree_x = 550
        if dino_y >= 110 and jump:
            dino_y -= 5
        else:
            jump = False
        if dino_y < 230 and not jump:
            dino_y += 5
        if dino_x == tree_x:
            score += 1
        show_score(score)
        gameplay = collision()
    else:
        show_score(score)
        screen.blit(over, (190, 110))
    pygame.display.update()