
import pygame
import time
import random
pygame.font.init()
pygame.mixer.init()

length,breadth = 1000,800
dis = pygame.display.set_mode((length,breadth))
pygame.display.set_caption("Hit it")

bg = pygame.transform.scale(pygame.image.load("C:/Users/debad/space.jpg"),(length,breadth)) # background image

player_length = 40                                #initialize vaariables
player_breadth = 60
player_velocity = 5
star_velocity = 3
star_length = 20
star_breadth = 30
bullet_velocity = 6
bullet_length = 5
bullet_breadth = 7

font = pygame.font.SysFont("comicsense", 30)

def draw(player,elapsed_time,stars,bullets,Score,breadth,player_breadth):                      # draw function
    dis.blit(bg,(0,0))
    time_text = font.render(f"time:{round(elapsed_time)}s",1,"white")
    dis.blit(time_text,(10,10))
    
    

    score_text = font.render(f"Score:{round(Score)}",1,"white")
    dis.blit(score_text,(10,40))
    
    
    #dis.blit(player,(200, breadth - player_breadth))
    pygame.draw.rect(dis,"white",player)      #color of rectangle
    
    
    for star in stars:
        pygame.draw.rect(dis,"red",star)
    for bullet in bullets:
        pygame.draw.rect(dis,"green",bullet)
    
    
    pygame.display.update()

def main():
    run = True
   # player = pygame.image.load("C:/Users/debad/ufp.png")
    player = pygame.Rect(200, breadth - player_breadth, player_length, player_breadth)
    player_y = 0
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    Score = 0
    next_bullet_threshold = 2
    
    shot = pygame.mixer.Sound("C:/Users/debad/whip.wav")
    star_add_increment = 2000
    star_count = 0
    
    stars = []
    bullets = []
    hit = False
    
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        
        if star_count > star_add_increment:
            for _ in range(1):
                star_x = random.randint(0, length-star_length)
                star = pygame.Rect(star_x,-star_breadth, star_length,star_breadth)
                stars.append(star)
                
            star_add_increment = max(200, star_add_increment - 30)  
            star_count = 0
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed() 
        
            
        if keys[pygame.K_LEFT] and player.x - player_velocity >= 0:     #change LEFT to any key on keyboard
            player.x -= player_velocity
        if keys[pygame.K_RIGHT] and player.x + player_velocity + player_length <= length:       #change RIGHT to any key on keyboard
            player.x += player_velocity
        if keys[pygame.K_UP] and player.y - player_velocity >= 0:        #change UP to any key on keyboard
            player.y -= player_velocity  
        if keys[pygame.K_DOWN] and player.y + player_velocity + player_breadth <= breadth:    #change DOWN to any key on keyboard
            player.y += player_velocity

                    
         
                
            
            
        for star in stars[:]:
            star.y += star_velocity
            if star.y > breadth:
                stars.remove(star)
            elif star.y + star_breadth >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
        
        if hit:
            lost_text = font.render("You Lost!",1,"white")
            dis.blit(lost_text, (length/2 - lost_text.get_width()/2, breadth/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        
        for bullet in bullets[:]:
            bullet.y -= bullet_velocity
            if bullet.y > breadth:
                bullets.remove(bullet)
            for star in stars[:]:
                if bullet.y + bullet_breadth >= star.y and bullet.colliderect(star):
                    stars.remove(star) 
                    Score = Score+50
                        
                
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_s] and current_time > next_bullet_threshold:
            shot.play()
            bullet = pygame.Rect(player.x, player.y, bullet_length, bullet_breadth)
            bullets.append(bullet) 
            bullet_delay = 500 # 500 milliseconds (0.5 seconds)
            next_bullet_threshold = current_time + bullet_delay
        
       
        
        
        
        
        draw(player,elapsed_time,stars,bullets,Score,breadth,player_breadth)    
    pygame.quit()
    
    
if __name__ == "__main__":
    main()
        