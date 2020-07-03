import sys
import time
import pygame
import random
from pygame.locals import *
from settings import Settings
red = (255,0,0)
black = (0,0,0)
white=(255,255,255)

# 기본적인 설정
pygame.init()
display_width = 1000
display_height = 773
screen= pygame.display.set_mode((1000,773))
pygame.display.set_caption("Soccer Game")
backGround = pygame.image.load("soccer.jpg")
backGroundImg = pygame.transform.scale(backGround,(1000,773))
clock = pygame.time.Clock()

pygame.display.flip()


def text_objects(text, font): # text 입력 함수
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None): # 버튼 만드는 함수
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)


def quit() :
    pygame.quit()
    quit()


def exitcode1_1() : # Kicker 게임 중, 미션을 성공했을때 나오는 화면
    intro = True
    while intro :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.blit(backGroundImg,(0,0))
        largeText = pygame.font.SysFont("comicsansms",75)
        TextSurf, TextRect = text_objects("Mission Complete!!!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)
        
        button("One More",200,450,100,50,red,black,entrycode1)
        button("Keeper",450,450,100,50,red,black,entrycode2)
        button("Exit",700,450,100,50,red,black,quit)
        
        pygame.display.update()
        clock.tick(15)  

        
def exitcode1_2() : # Kicker 게임 중, 미션을 실패했을때 나오는 화면
    intro = True
    while intro :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.blit(backGroundImg,(0,0))
        largeText = pygame.font.SysFont("comicsansms",75)
        TextSurf, TextRect = text_objects("Mission Failed...", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)
        
        button("One More",200,450,100,50,red,black,entrycode1)
        button("Keeper",450,450,100,50,red,black,entrycode2)
        button("Exit",700,450,100,50,red,black,quit)
        
        pygame.display.update()
        clock.tick(15)  

def exitcode2_1() : # Keeper 게임 중, 미션을 성공했을때 나오는 화면
    intro = True
    while intro :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.blit(backGroundImg,(0,0))
        largeText = pygame.font.SysFont("comicsansms",75)
        TextSurf, TextRect = text_objects("Mission Complete!!!", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)
        
        button("One More",200,450,100,50,red,black,entrycode2)
        button("Kicker",450,450,100,50,red,black,entrycode1)
        button("Exit",700,450,100,50,red,black,quit)
        
        pygame.display.update()
        clock.tick(15)  

def exitcode2_2() : # Keeper 게임 중, 미션을 실패했을때 나오는 화면
    intro = True
    while intro :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.blit(backGroundImg,(0,0))
        largeText = pygame.font.SysFont("comicsansms",75)
        TextSurf, TextRect = text_objects("Mission Failed...", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)
        
        button("One More",200,450,100,50,red,black,entrycode2)
        button("Kicker",450,450,100,50,red,black,entrycode1)
        button("Exit",700,450,100,50,red,black,quit)
        
        pygame.display.update()
        clock.tick(15)  



def entrycode1() : # Kicker 게임 시작 
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.width, ai_settings.height))
    keys = [False, False, False, False, False] #움직이기 위한 key 정의
    kickerPos = [500,600] # 좌표 설정
    ballPos = [500,500]
    goalPos = [276,20]
    score = 0
    game_over = False
    keeper1Pos=[500,40]
    keeper2Pos=[random.randint(150,900),random.randint(25,400)] # keeper들 랜덤으로 배정
    keeper3Pos=[random.randint(150,900),random.randint(25,400)]
    keeper4Pos=[random.randint(150,900),random.randint(25,400)]
    keeper5Pos=[random.randint(150,900),random.randint(25,400)]
    keeper6Pos=[random.randint(150,900),random.randint(25,400)]


    pygame.mixer.init()

    # 이미지 불러오기
    kicker = pygame.image.load("kicker.png")
    keep1 = pygame.image.load("keeper.png")
    keep2 = pygame.image.load("keeper.png")
    keep3 = pygame.image.load("keeper.png")
    keep4 = pygame.image.load("keeper.png")
    keep5 = pygame.image.load("keeper.png")
    keep6 = pygame.image.load("keeper.png")

    backGround = pygame.image.load("soccer.jpg") 
    endingImg = pygame.image.load("soccer.jpg")
    ball = pygame.image.load("football.png")
    goalpost = pygame.image.load('goalpost.png')
    screen.blit(screen,(0,0))
    pygame.display.flip()

    backGroundImg = pygame.transform.scale(backGround,(1000,773)) 
  
    running = 1
    exitcode = 0 #화면 전환을 위함
    total_time = 50 # 정해진 시간
    start_ticks = pygame.time.get_ticks() # 시작하는 시간 저장

    while running :
        screen.fill(0)
        screen.blit(backGroundImg,(0,0))
        screen.blit(kicker,kickerPos)
        screen.blit(goalpost, goalPos)
        screen.blit(ball,ballPos)    
        screen.blit(keep1,keeper1Pos)
        screen.blit(keep2,keeper2Pos)
        screen.blit(keep3,keeper3Pos)
        screen.blit(keep4,keeper4Pos)
        screen.blit(keep5,keeper5Pos)
        screen.blit(keep6,keeper6Pos)

        font = pygame.font.Font(None, 30)
        scoretext = font.render('Your Score : %d'%score,True,(200,0,0))
        textRect = scoretext.get_rect()
        textRect.topright=[900,10]
        screen.blit(scoretext, textRect)
        
        missiontxt=font.render("Mission : Goal=5",True,(0,0,200))
        missionrect=missiontxt.get_rect()
        missionrect.topright=[600,25]
        screen.blit(missiontxt,missionrect)
        
        #시간 설정
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        timertxt = font.render("TIME : {}".format(int(total_time - elapsed_time)), True, (200,200,100))
        timeRect = timertxt.get_rect()
        timeRect.topright=[100,15]
        screen.blit(timertxt, timeRect)
        
        # keeper들 랜덤으로 배정 후 움직이게 하기 
        keeper1_speed = int(random.choice([-5,5]))
        keeper2_speed = int(random.choice([-5,5]))
        keeper3_speed = int(random.choice([-5,5]))
        keeper4_speed = int(random.choice([-5,5]))
        keeper5_speed = int(random.choice([-5,5]))
        keeper6_speed = int(random.choice([-5,5]))
        keeper1Pos[0]+=keeper1_speed
        keeper2Pos[0]+=keeper2_speed
        keeper3Pos[0]+=keeper3_speed
        keeper4Pos[0]+=keeper4_speed
        keeper5Pos[0]+=keeper5_speed
        keeper6Pos[0]+=keeper6_speed
        # 만약 keeper들이 움직이다가 화면 밖으로 나가면 다시 배정
        if keeper1Pos[0] >1005 or keeper1Pos[0]<-5 :
            keeper1Pos=[random.randint(150,900),random.randint(25,400)]
        if keeper2Pos[0] >1005 or keeper2Pos[0]<-5 :
            keeper2Pos=[random.randint(150,900),random.randint(25,400)]
        if keeper3Pos[0] >1005 or keeper3Pos[0]<-5 :
            keeper3Pos=[random.randint(150,900),random.randint(25,400)]
        if keeper4Pos[0] >1005 or keeper4Pos[0]<-5 :
            keeper4Pos=[random.randint(150,900),random.randint(25,400)]
        if keeper5Pos[0] >1005 or keeper5Pos[0]<-5 :
            keeper5Pos=[random.randint(150,900),random.randint(25,400)]
        if keeper6Pos[0] >1005 or keeper6Pos[0]<-5 :
            keeper6Pos=[random.randint(150,900),random.randint(25,400)]
            
        
        
        
        # 공이 나가면 다시 중앙으로
        if ballPos[0] > 1005 :
            ballPos = [500,500]
        elif ballPos[0] < -5 :
            ballPos = [500,500]
        elif ballPos[1] < -5 :
            ballPos = [500,500]
        elif ballPos[1] > 775 :
            ballPos = [500,500]
        
        kicker_rect = kicker.get_rect()
        kicker_rect.left = kickerPos[0]
        kicker_rect.top = kickerPos[1]

        ball_rect= ball.get_rect()
        ball_rect.left = ballPos[0]
        ball_rect.top = ballPos[1]
        
        goalpost_rect = goalpost.get_rect()
        goalpost_rect.left = goalPos[0]
        goalpost_rect.top = goalPos[1]       

        keep1_rect = keep1.get_rect()
        keep1_rect.left = keeper1Pos[0]
        keep1_rect.top = keeper1Pos[1]

        keep2_rect = keep2.get_rect()
        keep2_rect.left = keeper2Pos[0]
        keep2_rect.top = keeper2Pos[1]
        
        keep3_rect = keep3.get_rect()
        keep3_rect.left = keeper3Pos[0]
        keep3_rect.top = keeper3Pos[1]

        keep4_rect = keep4.get_rect()
        keep4_rect.left = keeper4Pos[0]
        keep4_rect.top = keeper4Pos[1]

        keep5_rect = keep5.get_rect()
        keep5_rect.left = keeper5Pos[0]
        keep5_rect.top = keeper5Pos[1]

        keep6_rect = keep6.get_rect()
        keep6_rect.left = keeper6Pos[0]
        keep6_rect.top = keeper6Pos[1]

        if ball_rect.colliderect(goalpost_rect) : # 골을 넣으면 점수 +1 하고 공 다시 원점
            score+=1
            ballPos=[500,500]

        if keep1_rect.colliderect(ball_rect) : # 공이 keeper와 충돌했다며 다시 원점 
            ballPos=[500,500]
            
        if keep2_rect.colliderect(ball_rect) :
            ballPos=[500,500]
            
        if keep3_rect.colliderect(ball_rect) :
            ballPos=[500,500]
            
        if keep4_rect.colliderect(ball_rect) :
            ballPos=[500,500]
            
        if keep5_rect.colliderect(ball_rect) :
            ballPos=[500,500]
            
        if keep6_rect.colliderect(ball_rect) :
            ballPos=[500,500]
            


    # 화면 업데이트
        pygame.display.flip()


    # key 역할 조절 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
    # 게임 끄기
                pygame.quit()
                exit(0)

                
            if event.type == pygame.KEYDOWN: #키가 눌렸는지 확인
                if event.key == K_UP:
                    keys[0] = True
                elif event.key == K_LEFT:
                    keys[1] = True
                elif event.key == K_DOWN:
                    keys[2] = True
                elif event.key == K_RIGHT:
                    keys[3] = True
                elif event.key == K_SPACE:
                    keys[4] = True

            if event.type == pygame.KEYUP: #키가 눌렸는지 확인
                if event.key == K_UP:
                    keys[0] = False
                elif event.key == K_LEFT:
                    keys[1] = False
                elif event.key == K_DOWN:
                    keys[2] = False
                elif event.key == K_RIGHT:
                    keys[3] = False
                elif event.key == K_SPACE:
                    keys[4] = False


    # 정해진 key에 대한 역할 정의
        if keys[0]:
            kickerPos[1]-=4
            if kicker_rect.colliderect(ball_rect): # 키를 움직임에 따라 공과 kicker과 접촉했다면 공이 움직임
                ballPos[1]-=3
        if keys[2]:
            kickerPos[1]+=4
            if kicker_rect.colliderect(ball_rect):
                ballPos[1]+=3
        if keys[1]:
            kickerPos[0]-=4
            if kicker_rect.colliderect(ball_rect):
                ballPos[0]-=3
        if keys[3]:
            kickerPos[0]+=4
            if kicker_rect.colliderect(ball_rect):
                ballPos[0]+=3
        if keys[4] :  # 스페이스를 누르면 발차기로 공이 더 움직이게 함
            if keys[0] :
                if kicker_rect.colliderect(ball_rect):
                    ballPos[1]-=100

            elif keys[2] :
                if kicker_rect.colliderect(ball_rect):
                    ballPos[1]+=100

            elif keys[3] :
                if kicker_rect.colliderect(ball_rect):
                    ballPos[0]+=100

            elif keys[1]:
                if kicker_rect.colliderect(ball_rect):
                    ballPos[0]-=100

            

        if score >= 5 :# 미션 5개 이상의 골을 넣었다면 게임을 끝내고 exitcode 1로 출력
            running = 0
            exitcode1_1()

        if total_time - elapsed_time <= 0 :# 시간이 지났다면 게임을 끝내고 exitcode 2로 출력
            running = 0
            exitcode1_2()

 
    while 1 : # 게임 끌때 어떻게 끌지 
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                exit(0)

            if score >= 5 :# 미션 5개 이상의 골을 넣었다면 게임을 끝내고 exitcode 1로 출력
                running = 0
                exitcode1_1()
                
            if total_time - elapsed_time <= 0 :# 시간이 지났다면 게임을 끝내고 exitcode 2로 출력
                running = 0
                exitcode1_2()

        pygame.display.flip()

def entrycode2() : # Keeperr 게임 시작
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.width, ai_settings.height))
    keys = [False, False, False, False] #움직이기 위한 key 정의
    kickerPos_x = int(random.randint(280,700))
    kickerPos_y = int(random.randint(400,600)) # kicker의 좌표를 랜덤으로 배정
    ballPos_x = kickerPos_x+3
    ballPos_y = kickerPos_y-3 # kicker에 따른 ball의 좌표도 맞춰 배정
    goalPos = [276,20]
    keeperPos = [490,50]
    score = 0
    keep_numbers = 0
    game_over = False
    ball_speed=25

    

    pygame.mixer.init()

    # 이미지 불러오기
    kicker = pygame.image.load("kicker.png")
    keeper = pygame.image.load("keeper.png")
    backGround = pygame.image.load("soccer.jpg") 
    endingImg = pygame.image.load("soccer.jpg")
    ball = pygame.image.load("football.png")
    goalpost = pygame.image.load('goalpost.png')
    screen.blit(screen,(0,0))
    pygame.display.flip()

    backGroundImg = pygame.transform.scale(backGround,(1000,773)) 
  
    running = 1
    exitcode = 0 #화면 전환을 위함
    total_time = 50 # 정해진 시간
    start_ticks = pygame.time.get_ticks() # 시작하는 시간 저장

    while running :
        screen.fill(0)
        screen.blit(backGroundImg,(0,0))
        screen.blit(goalpost, goalPos)
        screen.blit(ball,(ballPos_x,ballPos_y))    
        screen.blit(keeper,keeperPos)
        screen.blit(kicker,(kickerPos_x,kickerPos_y))
        font = pygame.font.Font(None, 30)
        scoretext = font.render('Rival\'s Score : %d'%score,True,(200,0,0))
        textRect = scoretext.get_rect()
        textRect.topright=[900,10]
        screen.blit(scoretext, textRect)
        keeptext= font.render('Your Score : %d' %keep_numbers, True,(200,0,0))
        txtRect = keeptext.get_rect()
        txtRect.topright=[900,40]
        screen.blit(keeptext, txtRect)
        font = pygame.font.Font(None,25)
        missiontxt=font.render("Mission :Your Score - Rival\'s Score >= 10",True,(0,0,200))
        missionrect=missiontxt.get_rect()
        missionrect.topright=[670,25]
        screen.blit(missiontxt,missionrect)
        font = pygame.font.Font(None, 30)
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        timertxt = font.render("TIME : {}".format(int(total_time - elapsed_time)), True, (200,200,100))
        timeRect = timertxt.get_rect()
        timeRect.topright=[100,15]
        screen.blit(timertxt, timeRect)
        # 공이 움직이는 속도
        ballPos_y-=5


        
        # 공이 나가면 다시 랜덤으로 배정
        if ballPos_x > 1005 :
            kickerPos_x = int(random.randint(280,700))
            kickerPos_y = int(random.randint(400,600))
            ballPos_x = kickerPos_x+3
            ballPos_y = kickerPos_y-3
        elif ballPos_x < -5 :
            kickerPos_x = int(random.randint(280,700))
            kickerPos_y = int(random.randint(400,600))
            ballPos_x = kickerPos_x+3
            ballPos_y = kickerPos_y-3
        elif ballPos_y < -5 :
            kickerPos_x = int(random.randint(280,700))
            kickerPos_y = int(random.randint(400,600))
            ballPos_x = kickerPos_x+3
            ballPos_y = kickerPos_y-3
        elif ballPos_y > 775 :
            kickerPos_x = int(random.randint(280,700))
            kickerPos_y = int(random.randint(400,600))
            ballPos_x = kickerPos_x+3
            ballPos_y = kickerPos_y-3
        
        kicker_rect = kicker.get_rect()
        kicker_rect.left = kickerPos_x
        kicker_rect.top = kickerPos_y
        
        keeper_rect = keeper.get_rect()
        keeper_rect.left = keeperPos[0]
        keeper_rect.top = keeperPos[1]
        
        ball_rect= ball.get_rect()
        ball_rect.left = ballPos_x
        ball_rect.top = ballPos_y
        
        goalpost_rect = goalpost.get_rect()
        goalpost_rect.left = goalPos[0]
        goalpost_rect.top = goalPos[1]       


                
        if ball_rect.colliderect(goalpost_rect) : # 골을 넣으면 상대방 점수 +1 하고 공 다시 원점
            kickerPos_x = int(random.randint(280,700))
            kickerPos_y = int(random.randint(400,600))
            ballPos_x = kickerPos_x+3
            ballPos_y = kickerPos_y-3
            score+=1
            
        elif ball_rect.colliderect(keeper_rect) : # 골키퍼가 공을 막으면 막은 횟수 +1하고 원점 
            kickerPos_x = int(random.randint(280,700))
            kickerPos_y = int(random.randint(400,600))
            ballPos_x = kickerPos_x+3
            ballPos_y = kickerPos_y-3
            keep_numbers +=1 
                
        
    # 화면 업데이트
        pygame.display.flip()


    # key 역할 조절 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
    # 게임 끄기
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN: #키가 눌렸는지 확인
                if event.key == K_UP:
                    keys[0] = True
                elif event.key == K_LEFT:
                    keys[1] = True
                elif event.key == K_DOWN:
                    keys[2] = True
                elif event.key == K_RIGHT:
                    keys[3] = True



            if event.type == pygame.KEYUP: #키가 눌렸는지 확인
                if event.key == K_UP:
                    keys[0] = False
                elif event.key == K_LEFT:
                    keys[1] = False
                elif event.key == K_DOWN:
                    keys[2] = False
                elif event.key == K_RIGHT:
                    keys[3] = False



    # 정해진 key에 대한 역할 정의
        if keys[0]:
            keeperPos[1]-=2.5 # y좌표 변경
        elif keys[2]:
            keeperPos[1]+=2.5 # y좌표 변경
        if keys[1]:
            keeperPos[0]-=2.5 # x좌표 변경
        elif keys[3]:
            keeperPos[0]+=2.5 # x좌표 변경


        
        
        if total_time - elapsed_time <= 0 :# 시간이 지났다면 게임을 끝내고 결과 확인
            running = 0
            if keep_numbers- score>= 10 : # 미션 상대방 점수와 내 점수가 10점 이상 차이난다면 미션 성공으로 exitcode1로 출력
                exitcode2_1()
            elif keep_numbers - score<10 : # 미션을 성공하지못했다면 exitcode2로 출력
                exitcode2_2()


        
    while 1 : # 게임 끌때 어떻게 끌지 
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                exit(0)

            if keep_numbers - score >=10 :# 미션 상대방 점수와 내 점수가 10점 이상 차이난다면 미션 성공으로 exitcode1로 출력
                running = 0
                exitcode2_1()   
                
            if keep_numbers - score < 10 :# 미션을 성공하지못했다면 exitcode2로 출력
                running = 0
                exitcode2_2()

        pygame.display.flip()


# 처음 게임 킬때 나오는 화면 (Kicker, Keeper, Exit 선택할 수 있도록 버튼 생성)
def game_intro():
    pygame.init()

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.blit(backGroundImg,(0,0))
        largeText = pygame.font.SysFont("comicsansms",75)
        font = pygame.font.Font(None, 60)
        protext = font.render('Welcome To Soccer Game!',True,(0,0,200))
        proRect = protext.get_rect()
        proRect.topright=[770,200]
        screen.blit(protext, proRect)
        
        
        TextSurf, TextRect = text_objects("What do you want to do?", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        button("Kicker",200,450,100,50,red,black,entrycode1)
        button("Keeper",450,450,100,50,red,black,entrycode2)
        button("Exit",700,450,100,50,red,black,quit)


        pygame.display.update()
        clock.tick(15)       

        
game_intro()