import pgzrun,random,time

HEIGHT,WIDTH,TITLE=700,700,"Connecting the Asteriods"
s=random.randint(15,20)
start_time,total_time,end_time=0,0,0
chances=3

start_time=time.time()
asteriods=[]

for i in range(s):
    A=Actor("asteriods")
    A.pos=random.randint(60,WIDTH-60),random.randint(60,HEIGHT-60)
    asteriods.append(A)

 
nextasteriods=0
lines=[]

def draw():
    global total_time,chances
    screen.blit("space2",(0,0))
    for i in range(s):
        asteriods[i].draw()
        screen.draw.text(str(i+1),(asteriods[i].pos[0],asteriods[i].pos[1]+20))
        screen.draw.text(str(round(chances,1)),(200,10),fontsize=60)
    for i in lines:
        screen.draw.line(i[0],i[1],"red")
    if nextasteriods<s:
        total_time=time.time()-start_time
        screen.draw.text(str(round(total_time,3)),(50,10),fontsize=50)
    else:
        print("hello")
        chances-=1
        screen.draw.text(str(round(chances,1)),(200,10),fontsize=60)
        print(str("Oops You missed it,Try again you still have {} Chances left".format(chances)),(70,10),fontsize=50)
        screen.draw.text(str(round(total_time,3)),(50,10),fontsize=50) 
        if chances==0:
           c=input("do you want more chances")
           if c=="yes":
            chances=3
           else:
               print("it's ok we can play later")
               breakpoint
           

def on_mouse_down(pos):
    global nextasteriods,lines
    if nextasteriods<s:
        if asteriods[nextasteriods].collidepoint(pos):
            if nextasteriods:
                lines.append((asteriods[nextasteriods-1].pos,asteriods[nextasteriods ].pos))
            nextasteriods+=1
        else:
            nextasteriods=0
            lines=[]
            

pgzrun.go()