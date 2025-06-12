import pgzrun,random,pyautogui
print(pyautogui.size())
WIDTH,HEIGHT,TITLE=pyautogui.size(),"SPACEWARS!"
w,h=WIDTH,HEIGHT



spaceship=Actor("spaceship")
spaceship.pos=(w,h-100)

def draw():
    spaceship.draw()



pgzrun.go()