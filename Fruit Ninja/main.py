import pgzrun
import random
import time

WIDTH, HEIGHT = 800, 600
TITLE =  "Fruit Ninja"
current_level = 1
final_level = 8
isGameOver = False
isGameComplete = False
Centre = (WIDTH/2, HEIGHT/2)
ITEM = ["bomb", "chair"]
items = []
animations = []
start_time = time.time()


def define_items(level):
    items_to_create = choose_items(level)
    new_actors = createActors(items_to_create)    
    layout_actors(new_actors)
    return new_actors


def displayMessage(msg1, msg2):
    global Centre
    screen.draw.text(msg1, color = (255,255,255) center= Centre, fontsize= 50) #experiment using fontname as a property fonts/filename.ttf
    screen.draw.text(msg2, color = (255,255,255), center = (Centre[0], Centre[1]+100), fontsize = 25)

def update():
    global items
    if len(items)==0:
        items = define_items(current_level)


def draw():
    global current_level, isGameOver, isGameComplete, items, start_time
    screen.clear()
    screen.blit("backgroundimg", (0,0))
    if isGameOver:
        displayMessage("Game Over", f"You got to level {current_level} and survived for {int(time.time()-start_time)}")
    elif isGameComplete:
        displayMessage("You win!", f"You beat the game in {int(time.time()-start_time)} seconds")
    else:
        for item in items:
            item.draw()


pgzrun.go()