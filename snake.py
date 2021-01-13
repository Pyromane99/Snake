#Package
import pygame
import random
while True:
    #Initialisation
    pygame.init()

    #Fenêtre
    win=pygame.display.set_mode((600,600))
    pygame.display.set_caption("Snake")


    clock=pygame.time.Clock()

    truc=True
    while truc :
        a=pygame.key.get_pressed()
        pygame.draw.rect(win,(255,0,0),(300,300,20,20))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                truc=False
                pygame.quit()
                
        if a[pygame.K_SPACE] :
            truc=False
        

    #Random
    def aléatoire():
        a=random.randint(0,15)
        b=random.randint(0,15)

        x=a*20
        y=b*20

        return x,y
    #Le serpent
    class snake(object):
        def __init__(self,position,heading,longueur,vel):
            self.longueur=longueur
            self.position=position
            self.len_tab=len(position)
            self.largeur=20
            self.vel=vel
            self.heading=heading
            self.x=position[self.len_tab-1][0]
            self.y=position[self.len_tab-1][1]
        
        def draw(self,win):
            for a in position:
                if a==(self.x,self.y):
                    pygame.draw.rect(win,(255,0,0),(a[0],a[1],self.largeur,self.largeur))
                else:
                    pygame.draw.rect(win,(0,0,255),(a[0],a[1],self.largeur,self.largeur))

        def avancement_tête(self):
            if self.heading == "Right":
                self.x=self.x+self.vel
            elif self.heading =="Left":
                self.x=self.x-self.vel
            elif self.heading=="Up":
                self.y=self.y-self.vel
            elif self.heading=="Down":
                self.y=self.y+self.vel
            self.position.append((self.x,self.y))

        def sup_queue(self):
            del position[0]

        def hitbox(self,x,y):
            if self.x==x and self.y==y:
                return True
            else:
                return False
            
    #la pomme
    class apple(object):
        def __init__(self,x,y):
            self.x=x
            self.y=y
            self.largeur=20

        def draw(self,win):
            pygame.draw.rect(win,(0,255,0),(self.x,self.y,self.largeur,self.largeur))
            
    #Dessin
    def dessin():
        win.fill((0,0,0))
        text=font.render("Score : "+str(score),1,(255,255,255))
        win.blit(text,(500,30)) 
        serpent1.draw(win)
        pomme1.draw(win)
        pygame.display.update()
        
    #Main Loop
    score=0
    a=0 
    font=pygame.font.SysFont('comicsans',20,True)
    position=[(300,300)]
    serpent1=snake(position,"Right",10,10)
    pomme1=apple(440,200)
    condition=True
    while(condition):
        a +=1
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                condition=False
                
        if serpent1.x > 600-serpent1.largeur or serpent1.x < 0 or serpent1.y >600-serpent1.largeur or serpent1.y <0 :
            condition=False
        compt=0
        for i in serpent1.position:
            compt+=1
            if compt !=len(serpent1.position):
                if serpent1.hitbox(i[0],i[1]):
                    condition=False
        
        if a%2 !=0:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and serpent1.heading !="Right":
                serpent1.heading="Left"
            elif keys[pygame.K_RIGHT] and serpent1.heading !="Left":
                serpent1.heading="Right"
            elif keys[pygame.K_UP] and serpent1.heading !="Down":
                serpent1.heading="Up"
            elif keys[pygame.K_DOWN] and serpent1.heading !="Up": 
                serpent1.heading="Down"
            
        serpent1.avancement_tête()

        if not serpent1.hitbox(pomme1.x,pomme1.y):
            serpent1.sup_queue()

        if serpent1.hitbox(pomme1.x,pomme1.y):
            pomme1.x,pomme1.y=aléatoire()
            score +=1 

        dessin()
    #Fermeture du jeu
    pygame.quit()
