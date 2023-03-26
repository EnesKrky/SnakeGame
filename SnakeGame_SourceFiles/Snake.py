#Controls:
    # W : UP
    # D : RIGHT
    # S : DOWN
    # A : LEFT
    # Q : QUIT
    # P : PAUSE
    # R : RESTART in 'game over' screen
import pygame,random,math
from pygame._sdl2.video import Window
pygame.init()

class slider:
    def __init__(self,centerx,centery,width,height,w,h,sradius,t,minv,maxv,sliderchannelcolor,slidercolor):
        self.centerx=centerx
        self.centery=centery
        self.width=width
        self.height=height
        self.w=w
        self.h=h
        self.sradius=sradius
        self.t=t
        self.minv=minv
        self.maxv=maxv
        self.SurfaceSliderchannel=pygame.Surface((self.width+self.height,self.height))
        self.SurfaceSliderchannel.set_colorkey((0,0,0))
        self.sliderchannelcolor=sliderchannelcolor
        pygame.draw.rect(self.SurfaceSliderchannel,self.sliderchannelcolor,(self.height/2,0,self.width,self.height))
        pygame.draw.circle(self.SurfaceSliderchannel,self.sliderchannelcolor,(self.height/2,self.height/2),self.height/2)
        pygame.draw.circle(self.SurfaceSliderchannel,self.sliderchannelcolor,(self.height/2+self.width,self.height/2),self.height/2)
        self.SurfaceSlider=pygame.Surface((self.w,self.h))
        self.SurfaceSlider.set_colorkey((0,0,0))
        self.slidercolor=slidercolor
        pygame.draw.rect(self.SurfaceSlider,self.slidercolor,(self.sradius,0,self.w-self.sradius*2,self.sradius))
        pygame.draw.rect(self.SurfaceSlider,self.slidercolor,(0,self.sradius,self.w,self.h-2*self.sradius))
        pygame.draw.rect(self.SurfaceSlider,self.slidercolor,(self.sradius,self.h-self.sradius,self.w-self.sradius*2,self.sradius))
        pygame.draw.circle(self.SurfaceSlider,self.slidercolor,(self.sradius,self.sradius),self.sradius)
        pygame.draw.circle(self.SurfaceSlider,self.slidercolor,(self.w-self.sradius,self.sradius),self.sradius)
        pygame.draw.circle(self.SurfaceSlider,self.slidercolor,(self.sradius,self.h-self.sradius),self.sradius)
        pygame.draw.circle(self.SurfaceSlider,self.slidercolor,(self.w-self.sradius,self.h-self.sradius),self.sradius)
    def control(self,changecontrol,b):
        old=self.t
        if mouse1 and (rgb[0],rgb[1],rgb[2])==self.slidercolor:
            mousedelta=pygame.mouse.get_pos()[0]-b[0]
            self.t=1-(self.width*(1-self.t)+mousedelta)/self.width
        if mouse1 and self.centerx+screen_x*0.2-self.width/2-self.height<pygame.mouse.get_pos()[0]<self.centerx+screen_x*0.2+self.width/2+self.height and self.centery+screen_y*0.05-self.height<pygame.mouse.get_pos()[1]<self.centery+screen_y*0.05+self.height:
            p=pygame.mouse.get_pos()[0]-(self.centerx+screen_x*0.2-self.width/2)
            self.t=1-p/self.width
        if self.t>=1:
            self.t=1
        elif self.t<=0:
            self.t=0
        if self.t!=old:
            changecontrol=True
        return changecontrol

def bait_pos():
    while len(tail)+1!=x*y:
        x_pos=random.randrange(x)
        y_pos=random.randrange(y)
        if [x_pos,y_pos] in tail or [x_pos,y_pos]==snake_head:
            continue
        else:
            break
    return x_pos,y_pos

def writesave():
    s=""
    s+="%d"%best_record+"\n"+"%f"%slider1.t+"\n"+"%d"%first_d
    f=open("save.txt","w")
    f.write(s)
    f.close()

"""def bot(direction):
    if direction==0 or (direction==1 and snake_head[0]==0):
        direction=2
    elif direction==2 and snake_head[0]==x-1:
        direction=1
    elif direction==1 and snake_head[0]==x-1:
        direction=4
    elif direction==4 and snake_head[0]==0:
        direction=1
    return direction"""

best_record=0
t1slider1=0.3
first_d=5
try:
    f=open("save.txt","r")
    data=f.read().split("\n")
    f.close()
    best_record=int(data[0])
    t1slider1=float(data[1])
    first_d=int(data[2])
except:
    pass
old_d=first_d
# 342x342,512x427,578x578,628x753,623x623,678x678,723x603,963x723,948x813
screen_sizes=[(20,20,15,15,2),(30,25,15,15,2),(25,25,20,20,3),(25,30,22,22,3),(20,20,28,28,3),(25,25,24,24,3),(30,25,21,21,3),(40,30,21,21,3),(35,30,24,24,3)]
resolutions=[]
for i in screen_sizes:
    s=""
    s+=str(i[4]+i[0]*(i[2]+i[4]))+"x"+str(i[4]+i[1]*(i[3]+i[4]))+" : "+str(i[0])+"x"+str(i[1])
    resolutions.append(s)
x,y=screen_sizes[first_d][0],screen_sizes[first_d][1]
w,h,t=screen_sizes[first_d][2],screen_sizes[first_d][3],screen_sizes[first_d][4]
screen_x=t+x*(w+t)
screen_y=t+y*(h+t)
sizeofmonitor=pygame.display.Info()
screen=pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption("SnakeGame")
window=Window.from_display_module()
window.position=(sizeofmonitor.current_w/2-screen_x/2,sizeofmonitor.current_h/2-screen_y/2)
pygame.display.set_icon(pygame.image.load("icon.ico"))

snake_head=[math.ceil(x/2),math.floor(y/2)]
head_direction=2
direction=0
tail=[[math.ceil(x/2)-1,math.floor(y/2)]]
tail_colors=[]
if len(tail)>0:
    last_tail=list(tail[len(tail)-1])
else:
    last_tail=[0,0]
new_tail=False
bait=bait_pos()
#baitcolors=[(220,50,30),(207,193,10),(9,217,172),(4,141,204),(130,154,176),(48, 69, 186)]
#currentbaitcolor=random.randrange(len(baitcolors))
baitcolor=(220,50,30)
colors=[((50,180,70),(121,182,46),(133,194,58),(131,186,3),(164,184,38),(209,181,25)),
        ((159,27,166),(138,33,113),(125,37,114),(130,23,166),(84,0,125),(125,2,153)),
        ((189,139,13),(176,95,4),(161,105,16),(186,103,2),(158,92,13),(163,119,8))]
head_colors=[(50,150,70),(99,9,102),(133,64,0)]
colorsetindex=random.randrange(len(colors))
for i in range(len(tail)):
    tail_colors.append(random.choice(colors[colorsetindex]))

slider1=slider(screen_x*0.53,screen_y*0.43,screen_x*0.3,screen_y*0.008,screen_x*0.03,screen_y*0.065,round(screen_y*0.006)+1,t1slider1,20,60,(50,100,50),(20,60,20))
slider2=slider(screen_x*0.53,screen_y*0.53,screen_x*0.3,screen_y*0.008,screen_x*0.03,screen_y*0.065,round(screen_y*0.006)+1,1-first_d/(len(screen_sizes)-1),0,len(screen_sizes)-1,(100,50,50),(60,20,20))
old_t=slider2.t

Surface1=pygame.Surface((round(screen_x*0.7),round(screen_y*0.8)))
Surface1.fill((170,170,170))
Surface2=pygame.Surface((round(screen_x*0.1),round(screen_y*0.8)-round(screen_x*0.2)))
Surface2.fill((170,170,170))
Surface3=pygame.Surface((round(screen_x*0.1),round(screen_x*0.1)))
pygame.draw.circle(Surface3,(170,170,170),(round(screen_x*0.1),round(screen_x*0.1)),round(screen_x*0.1))
Surface4=pygame.Surface((round(screen_x*0.1),round(screen_x*0.1)))
pygame.draw.circle(Surface4,(170,170,170),(round(screen_x*0.1),0),round(screen_x*0.1))
Surface5=pygame.Surface((round(screen_x*0.8),round(screen_y*0.8)))
Surface5.set_colorkey((0,0,0))
Surface5.set_alpha(230)
Surface5.blit(Surface1,(round(screen_x*0.1)+2,0),special_flags=pygame.BLEND_RGBA_MAX)
Surface5.blit(Surface2,(3,round(screen_x*0.1)),special_flags=pygame.BLEND_RGBA_MAX)
Surface5.blit(Surface3,(3,1),special_flags=pygame.BLEND_RGBA_MAX)
Surface5.blit(Surface4,(3,round(screen_y*0.8)-round(screen_x*0.1)-1),special_flags=pygame.BLEND_RGBA_MAX)
Surface5.blit(slider1.SurfaceSliderchannel,(slider1.centerx-slider1.width/2-slider1.height/2,slider1.centery-slider1.height/2))
Surface5.blit(slider2.SurfaceSliderchannel,(slider2.centerx-slider2.width/2-slider2.height/2,slider2.centery-slider2.height/2))

Surface6=pygame.Surface((round(screen_x*0.3),round(screen_y*0.1)))
Surface6.set_colorkey((0,0,0))
Surface6.set_alpha(230)
Surface7=pygame.Surface((round(screen_x*0.27),round(screen_y*0.1)))
Surface7.fill((170,170,170))
Surface8=pygame.Surface((round(screen_x*0.03),round(screen_y*0.1)-round(screen_x*0.06)))
Surface8.fill((170,170,170))
Surface9=pygame.Surface((round(screen_x*0.03),round(screen_x*0.03)))
pygame.draw.circle(Surface9,(170,170,170),(0,round(screen_x*0.03)),round(screen_x*0.03))
Surface10=pygame.Surface((round(screen_x*0.03),round(screen_x*0.03)))
pygame.draw.circle(Surface10,(170,170,170),(0,0),round(screen_x*0.03))
Surface6.blit(Surface7,(-2,0),special_flags=pygame.BLEND_RGBA_MAX)
Surface6.blit(Surface8,(round(screen_x*0.27)-3,round(screen_x*0.03)),special_flags=pygame.BLEND_RGBA_MAX)
Surface6.blit(Surface9,(round(screen_x*0.27)-3,1),special_flags=pygame.BLEND_RGBA_MAX)
Surface6.blit(Surface10,(round(screen_x*0.27)-3,round(screen_y*0.1)-round(screen_x*0.03)-1),special_flags=pygame.BLEND_RGBA_MAX)

animation1=0
animation_time1=0.6 # total time taken in second while 'game over' screen is opening or closing
timer1=0
time1=0
animation1_x=screen_x
animation2_x=0
pauseperiod=3

pygame.font.init()
font1=pygame.font.SysFont("sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic",int(screen_x*0.08))
font2=pygame.font.SysFont("sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic",int(screen_x*0.05))
font3=pygame.font.SysFont("impact",int(screen_x*0.048))
font4=pygame.font.SysFont("sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic",int(screen_x*0.2))
font5=pygame.font.SysFont("impact",int(screen_x*0.07))
font6=pygame.font.SysFont("impact",int(screen_x*0.045))
font7=pygame.font.SysFont("davidlibre",int(screen_x*0.05))
gameovertext=font1.render("GAME OVER",True,(0,0,0))
gameovertext.set_alpha(230)
gameovertext_rect=gameovertext.get_rect()
gameovertext_rect.center=(screen_x*0.44,screen_y*0.08)
recordtext=font2.render("Score",True,(0,0,0))
recordtext.set_alpha(230)
recordtext_rect=recordtext.get_rect()
recordtext_rect.center=(screen_x*0.23,screen_y*0.2)
bestrecordtext=font2.render("Best Score",True,(0,0,0))
bestrecordtext.set_alpha(230)
bestrecordtext_rect=bestrecordtext.get_rect()
bestrecordtext_rect.center=(screen_x*0.56,screen_y*0.2)
Surface5.blit(bestrecordtext,bestrecordtext_rect)
Surface5.blit(recordtext,recordtext_rect)
Surface5.blit(gameovertext,gameovertext_rect)
nametagtext=font3.render("Made by Enes",True,(0,0,0))
nametagtext.set_alpha(230)
nametagtext_rect=nametagtext.get_rect()
nametagtext_rect.center=(screen_x*0.15,screen_y*0.05)
Surface6.blit(nametagtext,nametagtext_rect)
pausetext=font4.render("PAUSED",True,(90,30,70))
pausetext.set_alpha(0)
pausetext_rect=pausetext.get_rect()
pausetext_rect.center=(screen_x*0.5,screen_y*0.5)
speedtext=font2.render("Speed:",True,(0,0,0))
speedtext.set_alpha(230)
speedtext_rect=speedtext.get_rect()
speedtext_rect.center=(screen_x*0.19,screen_y*0.43)
dimensionstext=font2.render("Dimensions:",True,(0,0,0))
dimensionstext.set_alpha(230)
dimensionstext_rect=dimensionstext.get_rect()
dimensionstext_rect.center=(screen_x*0.19,screen_y*0.53)
mintext=font5.render("-",True,(0,0,0))
mintext.set_alpha(230)
mintext_rect=mintext.get_rect()
mintext_rect.center=(screen_x*0.32,screen_y*0.422)
maxtext=font5.render("+",True,(0,0,0))
maxtext.set_alpha(230)
maxtext_rect=maxtext.get_rect()
maxtext_rect.center=(screen_x*0.74,screen_y*0.427)
restext=font6.render(resolutions[first_d],True,(0,0,0))
restext.set_alpha(230)
restext_rect=restext.get_rect()
restext_rect.center=(slider2.centerx,slider2.centery+screen_y*0.08)
restarttext=font7.render("Restart (R)",True,(0,0,0))
restarttext.set_alpha(230)
restarttext_rect=restarttext.get_rect()
restarttext_rect.center=(screen_x*0.44,screen_y*0.72)
Surface5.blit(speedtext,speedtext_rect)
Surface5.blit(dimensionstext,dimensionstext_rect)
Surface5.blit(mintext,mintext_rect)
Surface5.blit(maxtext,maxtext_rect)
Surface5.blit(restext,restext_rect)
Surface5.blit(restarttext,restarttext_rect)

record=0
old_record=1
t1=pygame.time.get_ticks()
fps=80
delay=slider1.t*(slider1.maxv-slider1.minv)+slider1.minv
mpos=[None,None]
rgb=(None,None,None)
final=False
changecontrol=False
mouse1=False
close=False
pause=False
game_over=False
screenchange=False
recordcontrol=False
while not close:
    if game_over:
        mpos=pygame.mouse.get_pos()
    pygame.time.Clock().tick(fps)
    if pygame.time.get_ticks()-t1>=delay:
        direction_control=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                close=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    close=True
                elif (event.key==pygame.K_w or event.key==pygame.K_UP) and direction!=3 and not direction_control and not animation1 and not pause:
                    direction=1
                    direction_control=True
                elif (event.key==pygame.K_d or event.key==pygame.K_RIGHT) and direction!=4 and not direction_control and not animation1 and not pause:
                    direction=2
                    direction_control=True
                elif (event.key==pygame.K_s or event.key==pygame.K_DOWN) and direction!=1 and not direction_control and not animation1 and not pause:
                    direction=3
                    direction_control=True
                elif (event.key==pygame.K_a or event.key==pygame.K_LEFT) and direction!=2 and direction!=0 and not direction_control and not animation1 and not pause:
                    direction=4
                    direction_control=True
                elif event.key==pygame.K_p and not game_over and not animation1 and direction:
                    pause=not pause
                    if pause:
                        time1=pygame.time.get_ticks()
                    else:
                        time1=0
                        timer1=0
                        pausetext.set_alpha(0)
                elif event.key==pygame.K_r and game_over and animation1==2:
                    snake_head=[math.ceil(x/2),math.floor(y/2)]
                    head_direction=2
                    direction=0
                    tail=[[math.ceil(x/2)-1,math.floor(y/2)]]
                    tail_colors=[]
                    colorsetindex=random.randrange(len(colors))
                    #currentbaitcolor=random.randrange(len(baitcolors))
                    tail_colors.append(random.choice(colors[colorsetindex]))
                    bait=bait_pos()
                    time1=pygame.time.get_ticks()
                    timer1=0
                    game_over=False
                    pause=False
                    changecontrol=False
                    mouse1=False
                    writesave()
                elif event.key==pygame.K_m:
                    game_over=True
                    pause=True
                    animation1=1
                    time1=pygame.time.get_ticks()
            if event.type==pygame.MOUSEBUTTONDOWN and game_over:
                if event.button==1:
                    rgb=screen.get_at(pygame.mouse.get_pos())
                    mouse1=True
            if event.type==pygame.MOUSEBUTTONUP and game_over:
                if event.button==1:
                    mouse1=False
        if animation1==1:
            timer1=(pygame.time.get_ticks()-time1)/1000
            animation1_x=screen_x*(1-0.8/(1+math.e**(5-10*timer1/animation_time1)))
            animation2_x=screen_x*0.3/(1+math.e**(5-10*timer1/animation_time1))
            if animation1_x<=0.205*screen_x:
                animation1_x=screen_x*0.2
                animation1=2
                timer1=0
                animation2_x=screen_x*0.3
                final=True
        elif animation1==2 and not game_over:
            timer1=(pygame.time.get_ticks()-time1)/1000
            animation1_x=screen_x*(0.2+0.8/(1+math.e**(5-10*timer1/animation_time1)))
            animation2_x=screen_x*0.3*(1-1/(1+math.e**(5-10*timer1/animation_time1)))
            if animation1_x>=0.994*screen_x:
                animation1_x=screen_x
                animation2_x=0
                animation1=0
                timer1=0
                record=0
                if old_t!=slider2.t:
                    screenchange=True
                    old_t=slider2.t
        if not pause and not animation1:
            #direction=bot(direction)
            if bait[0]==snake_head[0] and bait[1]==snake_head[1]:
                bait=bait_pos()
                #currentbaitcolor=random.randrange(len(baitcolors))
                record+=1
                if len(tail)==0:
                    tail.append([snake_head[0],snake_head[1]])
                else:
                    new_tail=True
            L=len(tail)
            """if direction==1 and snake_head[1]>0 and [snake_head[0],snake_head[1]-1] in tail:
                game_over=True
            elif direction==1 and snake_head[1]==0 and [snake_head[0],y-1] in tail:
                game_over=True
            elif direction==2 and snake_head[0]<x-1 and [snake_head[0]+1,snake_head[1]] in tail:
                game_over=True
            elif direction==2 and snake_head[0]==x-1 and [0,snake_head[1]] in tail:
                game_over=True
            elif direction==3 and snake_head[1]<y-1 and [snake_head[0],snake_head[1]+1] in tail:
                game_over=True
            elif direction==3 and snake_head[1]==y-1 and [snake_head[0],0] in tail:
                game_over=True
            elif direction==4 and snake_head[0]>0 and [snake_head[0]-1,snake_head[1]] in tail:
                game_over=True
            elif direction==4 and snake_head[0]==0 and [x-1,snake_head[1]] in tail:
                game_over=True"""
            if L>0 and direction:
                last_tail[0],last_tail[1]=tail[L-1][0],tail[L-1][1]
            if L>1 and direction and not game_over:
                for z in list(reversed(range(1,L))):
                    tail[z][0],tail[z][1]=tail[z-1][0],tail[z-1][1]
            if L>=1 and direction and not game_over:
                tail[0][0],tail[0][1]=snake_head[0],snake_head[1]
            if new_tail:
                tail.append([last_tail[0],last_tail[1]])
                tail_colors.append(random.choice(colors[colorsetindex]))
                new_tail=False
            if direction==1 and snake_head[1]>0 and not game_over:
                snake_head[1]-=1
            elif direction==1 and snake_head[1]==0 and not game_over:
                snake_head[1]=y-1
            elif direction==2 and snake_head[0]<x-1 and not game_over:
                snake_head[0]+=1
            elif direction==2 and snake_head[0]==x-1 and not game_over:
                snake_head[0]=0
            elif direction==3 and snake_head[1]<y-1 and not game_over:
                snake_head[1]+=1
            elif direction==3 and snake_head[1]==y-1 and not game_over:
                snake_head[1]=0
            elif direction==4 and snake_head[0]>0 and not game_over:
                snake_head[0]-=1
            elif direction==4 and snake_head[0]==0 and not game_over:
                snake_head[0]=x-1
            if L>0:
                if tail[0][1]-snake_head[1]==1 or (tail[0][1]==0 and snake_head[1]==y-1):
                    head_direction=1
                elif snake_head[0]-tail[0][0]==1 or (tail[0][0]==x-1 and snake_head[0]==0):
                    head_direction=2
                elif snake_head[1]-tail[0][1]==1 or (tail[0][1]==y-1 and snake_head[1]==0):
                    head_direction=3
                elif tail[0][0]-snake_head[0]==1 or (tail[0][0]==0 and snake_head[0]==x-1):
                    head_direction=4
            if snake_head in tail or len(tail)+1==x*y:
                game_over=True
            t1=pygame.time.get_ticks()
        if (game_over and not pause and not animation1) or changecontrol:
            if game_over and not pause and not animation1:
                pause=True
                animation1=1
                time1=pygame.time.get_ticks()
            if record>best_record:
                best_record=record
            Surface5.set_colorkey((0,0,0))
            Surface5.set_alpha(230)
            Surface5.blit(Surface1,(round(screen_x*0.1)+2,0),special_flags=pygame.BLEND_RGBA_MAX)
            Surface5.blit(Surface2,(3,round(screen_x*0.1)),special_flags=pygame.BLEND_RGBA_MAX)
            Surface5.blit(Surface3,(3,1),special_flags=pygame.BLEND_RGBA_MAX)
            Surface5.blit(Surface4,(3,round(screen_y*0.8)-round(screen_x*0.1)-1),special_flags=pygame.BLEND_RGBA_MAX)
            Surface5.blit(slider1.SurfaceSliderchannel,(slider1.centerx-slider1.width/2-slider1.height/2,slider1.centery-slider1.height/2))
            Surface5.blit(slider2.SurfaceSliderchannel,(slider2.centerx-slider2.width/2-slider2.height/2,slider2.centery-slider2.height/2))
            recordnumber=font3.render("%d"%record,True,(0,0,0))
            recordnumber.set_alpha(230)
            recordnumber_rect=recordnumber.get_rect()
            recordnumber_rect.center=(screen_x*0.23,screen_y*0.3)
            Surface5.blit(recordnumber,recordnumber_rect)
            bestrecordnumber=font3.render("%d"%best_record,True,(0,0,0))
            bestrecordnumber.set_alpha(230)
            bestrecordnumber_rect=bestrecordnumber.get_rect()
            bestrecordnumber_rect.center=(screen_x*0.56,screen_y*0.3)
            Surface5.blit(bestrecordnumber,bestrecordnumber_rect)
            Surface5.blit(bestrecordtext,bestrecordtext_rect)
            Surface5.blit(recordtext,recordtext_rect)
            Surface5.blit(gameovertext,gameovertext_rect)
            Surface5.blit(speedtext,speedtext_rect)
            Surface5.blit(dimensionstext,dimensionstext_rect)
            Surface5.blit(mintext,mintext_rect)
            Surface5.blit(maxtext,maxtext_rect)
            Surface5.blit(restext,restext_rect)
            Surface5.blit(restarttext,restarttext_rect)
    if game_over:
        changecontrol=slider1.control(changecontrol,mpos)
        changecontrol=slider2.control(changecontrol,mpos)
    if (animation1==2 and not game_over) or animation1==1 or animation1==0 or changecontrol or final:
        final=False
        L=len(tail)
        screen.fill((255,255,255))
        pygame.draw.circle(screen,baitcolor,(t+bait[0]*(w+t)+w/2,t+bait[1]*(h+t)+h/2),w/2)
        for k in range(len(tail)):
            pygame.draw.rect(screen,tail_colors[k],(t+tail[k][0]*(w+t),t+tail[k][1]*(h+t),w,h))
        pygame.draw.rect(screen,head_colors[colorsetindex],(t+snake_head[0]*(w+t),t+snake_head[1]*(h+t),w,h))
        if L>0:
            bx=t+snake_head[0]*(w+t)
            by=t+snake_head[1]*(h+t)
            br=(w**2/4+h**2/16)**0.5+1
            r=(w**2/4+h**2/16)**0.5/3*2.4
            if head_direction==1:
                pygame.draw.circle(screen,head_colors[colorsetindex],(bx+w/2,by+h/4),br)
                pygame.draw.circle(screen,head_colors[colorsetindex],(bx+w/4,by+h/2),r)
                pygame.draw.circle(screen,head_colors[colorsetindex],(bx+3*w/4,by+h/2),r)
            elif head_direction==2:
                pygame.draw.circle(screen,head_colors[colorsetindex],(bx+3*w/4,by+h/2),br)
                pygame.draw.circle(screen,head_colors[colorsetindex],(bx+w/2,by+h/4),r)
                pygame.draw.circle(screen,head_colors[colorsetindex],(bx+w/2,by+3*h/4),r)
            elif head_direction==3:
                pygame.draw.circle(screen,head_colors[colorsetindex],(bx+w/2,by+3*h/4),br)
                pygame.draw.circle(screen,head_colors[colorsetindex],(bx+w/4,by+h/2),r)
                pygame.draw.circle(screen,head_colors[colorsetindex],(bx+3*w/4,by+h/2),r)
            elif head_direction==4:
                pygame.draw.circle(screen,head_colors[colorsetindex],(bx+w/4,by+h/2),br)
                pygame.draw.circle(screen,head_colors[colorsetindex],(bx+w/2,by+h/4),r)
                pygame.draw.circle(screen,head_colors[colorsetindex],(bx+w/2,by+3*h/4),r)
        if animation1_x<screen_x:
            screen.blit(Surface5,(animation1_x,screen_y*0.05))
            screen.blit(Surface6,(animation2_x-screen_x*0.3,screen_y*0.875))
            screen.blit(slider1.SurfaceSlider,(animation1_x+slider1.centerx-slider1.width/2+(1-slider1.t)*slider1.width-slider1.w/2,screen_y*0.05+slider1.centery-slider1.h/2))
            dist=[]
            for k in range(slider2.maxv+1):
                dist.append((k/slider2.maxv-slider2.t)**2)
            step=dist.index(min(dist))
            slider2.t=step/slider2.maxv
            for z in range(len(screen_sizes)):
                pygame.draw.rect(screen,(0,0,0),(animation1_x+slider2.centerx-slider2.width/2+slider2.width*z/(len(screen_sizes)-1)-screen_x*0.0035,screen_y*0.05+slider2.centery-screen_y*0.01,screen_x*0.007,screen_y*0.02))
            screen.blit(slider2.SurfaceSlider,(animation1_x+slider2.centerx-slider2.width/2+(1-slider2.t)*slider2.width-slider2.w/2,screen_y*0.05+slider2.centery-slider2.h/2))
        else:
            if record>best_record:
                    best_record=record
            if old_record!=record or recordcontrol:
                rtext=font2.render("%d"%record,True,(120,120,120))
                brtext=font2.render("%d"%best_record,True,(120,120,120))
                rtext.set_alpha(200)
                brtext.set_alpha(200)
                rtext_rect=rtext.get_rect()
                brtext_rect=brtext.get_rect()
                rtext_rect[0]=screen_x*0.01
                rtext_rect[1]=screen_y*0.008
                brtext_rect[0]=screen_x*0.99-brtext_rect[2]
                brtext_rect[1]=screen_y*0.008
                old_record=record
                if recordcontrol:
                    recordcontrol=False
            screen.blit(rtext,rtext_rect)
            screen.blit(brtext,brtext_rect)
        if changecontrol:
            delay=slider1.t*(slider1.maxv-slider1.minv)+slider1.minv
            changecontrol=False
            first_d=round((1-slider2.t)*slider2.maxv)
            if old_d!=first_d:
                restext=font6.render(resolutions[first_d],True,(0,0,0))
                restext.set_alpha(230)
                restext_rect=restext.get_rect()
                restext_rect.center=(slider2.centerx,slider2.centery+screen_y*0.08)
                old_d=first_d
                changecontrol=True
    if pause and not game_over:
        timer1=(pygame.time.get_ticks()-time1)/1000
        if timer1<=0.35*pauseperiod:
            pausetext.set_alpha(int(250*math.sin(math.pi/(0.7*pauseperiod)*timer1)))
        elif 0.9*pauseperiod>=timer1>=0.55*pauseperiod:
            pausetext.set_alpha(int(250*math.sin(math.pi/(0.7*pauseperiod)*(timer1-0.2*pauseperiod))))
        elif timer1>=0.9*pauseperiod:
            pausetext.set_alpha(0)
        if timer1>=pauseperiod:
            timer1=0
            time1=pygame.time.get_ticks()
        screen.blit(pausetext,pausetext_rect)
    pygame.display.update()
    if screenchange:
        first_d=round((1-slider2.t)*slider2.maxv)
        old_d=first_d
        x,y=screen_sizes[first_d][0],screen_sizes[first_d][1]
        w,h,t=screen_sizes[first_d][2],screen_sizes[first_d][3],screen_sizes[first_d][4]
        screen_x=t+x*(w+t)
        screen_y=t+y*(h+t)
        screen=pygame.display.set_mode((screen_x,screen_y))
        window.position=(sizeofmonitor.current_w/2-screen_x/2,sizeofmonitor.current_h/2-screen_y/2)
        snake_head=[math.ceil(x/2),math.floor(y/2)]
        tail=[[math.ceil(x/2)-1,math.floor(y/2)]]
        bait=bait_pos()
        slider1=slider(screen_x*0.53,screen_y*0.43,screen_x*0.3,screen_y*0.008,screen_x*0.03,screen_y*0.065,round(screen_y*0.006)+1,slider1.t,round(20*25/min((x,y))),round(60*25/min((x,y))),(50,100,50),(20,60,20))
        slider2=slider(screen_x*0.53,screen_y*0.53,screen_x*0.3,screen_y*0.008,screen_x*0.03,screen_y*0.065,round(screen_y*0.006)+1,slider2.t,slider1.minv,slider2.maxv,(100,50,50),(60,20,20))
        delay=slider1.t*(slider1.maxv-slider1.minv)+slider1.minv
        Surface1=pygame.Surface((round(screen_x*0.7),round(screen_y*0.8)))
        Surface1.fill((170,170,170))
        Surface2=pygame.Surface((round(screen_x*0.1),round(screen_y*0.8)-round(screen_x*0.2)))
        Surface2.fill((170,170,170))
        Surface3=pygame.Surface((round(screen_x*0.1),round(screen_x*0.1)))
        pygame.draw.circle(Surface3,(170,170,170),(round(screen_x*0.1),round(screen_x*0.1)),round(screen_x*0.1))
        Surface4=pygame.Surface((round(screen_x*0.1),round(screen_x*0.1)))
        pygame.draw.circle(Surface4,(170,170,170),(round(screen_x*0.1),0),round(screen_x*0.1))
        Surface5=pygame.Surface((round(screen_x*0.8),round(screen_y*0.8)))
        Surface5.set_colorkey((0,0,0))
        Surface5.set_alpha(230)
        Surface5.blit(Surface1,(round(screen_x*0.1)+2,0),special_flags=pygame.BLEND_RGBA_MAX)
        Surface5.blit(Surface2,(3,round(screen_x*0.1)),special_flags=pygame.BLEND_RGBA_MAX)
        Surface5.blit(Surface3,(3,1),special_flags=pygame.BLEND_RGBA_MAX)
        Surface5.blit(Surface4,(3,round(screen_y*0.8)-round(screen_x*0.1)-1),special_flags=pygame.BLEND_RGBA_MAX)
        Surface5.blit(slider1.SurfaceSliderchannel,(slider1.centerx-slider1.width/2-slider1.height/2,slider1.centery-slider1.height/2))
        Surface5.blit(slider2.SurfaceSliderchannel,(slider2.centerx-slider2.width/2-slider2.height/2,slider2.centery-slider2.height/2))
        Surface6=pygame.Surface((round(screen_x*0.3),round(screen_y*0.1)))
        Surface6.set_colorkey((0,0,0))
        Surface6.set_alpha(230)
        Surface7=pygame.Surface((round(screen_x*0.27),round(screen_y*0.1)))
        Surface7.fill((170,170,170))
        Surface8=pygame.Surface((round(screen_x*0.03),round(screen_y*0.1)-round(screen_x*0.06)))
        Surface8.fill((170,170,170))
        Surface9=pygame.Surface((round(screen_x*0.03),round(screen_x*0.03)))
        pygame.draw.circle(Surface9,(170,170,170),(0,round(screen_x*0.03)),round(screen_x*0.03))
        Surface10=pygame.Surface((round(screen_x*0.03),round(screen_x*0.03)))
        pygame.draw.circle(Surface10,(170,170,170),(0,0),round(screen_x*0.03))
        Surface6.blit(Surface7,(-2,0),special_flags=pygame.BLEND_RGBA_MAX)
        Surface6.blit(Surface8,(round(screen_x*0.27)-3,round(screen_x*0.03)),special_flags=pygame.BLEND_RGBA_MAX)
        Surface6.blit(Surface9,(round(screen_x*0.27)-3,1),special_flags=pygame.BLEND_RGBA_MAX)
        Surface6.blit(Surface10,(round(screen_x*0.27)-3,round(screen_y*0.1)-round(screen_x*0.03)-1),special_flags=pygame.BLEND_RGBA_MAX)
        animation1_x=screen_x
        pygame.font.init()
        font1=pygame.font.SysFont("sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic",int(screen_x*0.08))
        font2=pygame.font.SysFont("sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic",int(screen_x*0.05))
        font3=pygame.font.SysFont("impact",int(screen_x*0.048))
        font4=pygame.font.SysFont("sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic",int(screen_x*0.2))
        font5=pygame.font.SysFont("impact",int(screen_x*0.07))
        font6=pygame.font.SysFont("impact",int(screen_x*0.045))
        font7=pygame.font.SysFont("davidlibre",int(screen_x*0.05))
        gameovertext=font1.render("GAME OVER",True,(0,0,0))
        gameovertext.set_alpha(230)
        gameovertext_rect=gameovertext.get_rect()
        gameovertext_rect.center=(screen_x*0.44,screen_y*0.08)
        recordtext=font2.render("Score",True,(0,0,0))
        recordtext.set_alpha(230)
        recordtext_rect=recordtext.get_rect()
        recordtext_rect.center=(screen_x*0.23,screen_y*0.2)
        bestrecordtext=font2.render("Best Score",True,(0,0,0))
        bestrecordtext.set_alpha(230)
        bestrecordtext_rect=bestrecordtext.get_rect()
        bestrecordtext_rect.center=(screen_x*0.56,screen_y*0.2)
        Surface5.blit(bestrecordtext,bestrecordtext_rect)
        Surface5.blit(recordtext,recordtext_rect)
        Surface5.blit(gameovertext,gameovertext_rect)
        nametagtext=font3.render("Made by Enes",True,(0,0,0))
        nametagtext.set_alpha(230)
        nametagtext_rect=nametagtext.get_rect()
        nametagtext_rect.center=(screen_x*0.15,screen_y*0.05)
        Surface6.blit(nametagtext,nametagtext_rect)
        pausetext=font4.render("PAUSED",True,(90,30,70))
        pausetext.set_alpha(0)
        pausetext_rect=pausetext.get_rect()
        pausetext_rect.center=(screen_x*0.5,screen_y*0.5)
        speedtext=font2.render("Speed:",True,(0,0,0))
        speedtext.set_alpha(230)
        speedtext_rect=speedtext.get_rect()
        speedtext_rect.center=(screen_x*0.19,screen_y*0.43)
        dimensionstext=font2.render("Dimensions:",True,(0,0,0))
        dimensionstext.set_alpha(230)
        dimensionstext_rect=dimensionstext.get_rect()
        dimensionstext_rect.center=(screen_x*0.19,screen_y*0.53)
        mintext=font5.render("-",True,(0,0,0))
        mintext.set_alpha(230)
        mintext_rect=mintext.get_rect()
        mintext_rect.center=(screen_x*0.32,screen_y*0.422)
        maxtext=font5.render("+",True,(0,0,0))
        maxtext.set_alpha(230)
        maxtext_rect=maxtext.get_rect()
        maxtext_rect.center=(screen_x*0.74,screen_y*0.427)
        restext=font6.render(resolutions[first_d],True,(0,0,0))
        restext.set_alpha(230)
        restext_rect=restext.get_rect()
        restext_rect.center=(slider2.centerx,slider2.centery+screen_y*0.08)
        restarttext=font7.render("Restart (R)",True,(0,0,0))
        restarttext.set_alpha(230)
        restarttext_rect=restarttext.get_rect()
        restarttext_rect.center=(screen_x*0.44,screen_y*0.72)
        Surface5.blit(speedtext,speedtext_rect)
        Surface5.blit(dimensionstext,dimensionstext_rect)
        Surface5.blit(mintext,mintext_rect)
        Surface5.blit(maxtext,maxtext_rect)
        Surface5.blit(restarttext,restarttext_rect)
        screenchange=False
        recordcontrol=True
writesave()
pygame.quit()
