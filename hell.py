import curses
import text_presets,utils
import time 
import json
import time 
import random

stdscr = curses.initscr()

def intro(screen):
    screen.clear()
    screen.addstr(0, 0,text_presets.HELLO)
    screen.refresh()
    time.sleep(1)

def hell_selection(screen):
    screen.clear()
    screen.addstr(0, 0,text_presets.MENU)
    start_pos_y,start_pos_x = (5,3)
    screen.move(start_pos_y,start_pos_x)
    while True:
        screen.refresh()
        key = screen.getch()
        pos_y,pos_x = screen.getyx()
        match key:
            case curses.KEY_DOWN:
                screen.move(pos_y+1,pos_x) if pos_y in range(start_pos_y,start_pos_y + 8) else None
            case curses.KEY_UP:
                screen.move(pos_y-1,pos_x) if pos_y in range(start_pos_y + 1,start_pos_y + 9) else None
            case 10:
                hell_n = screen.inch(pos_y,pos_x)
                screen.clear()
                return chr(hell_n)
            case 113: 
                break
            case other:
                pass
def infinite_hell(screen):
    while True:
        hell_n = random.randint(1,8)
        with open(f"CirclesOfRegEx/{hell_n}.json","r") as out:
            hell = json.load(out)
        challange = random.choice(hell) 
        
        score = 0
        after_x_lines_render = challange['match'].count('\n')+1
        
        screen.addstr(0,0,challange["description"])
        screen.addstr(1,0,challange["match"])
        screen.addstr(after_x_lines_render,0,"\n")
        screen.addstr(after_x_lines_render+1,0,"Type your regex!\n")
        
        start_time = time.time()

        usr_in = utils.get_user_in(screen)
        screen.clear()
        
        if utils.test(usr_in,challange["match"],challange["result"]): 
            screen.addstr(0,0,"Conquered !")
            score+=1
        else:
            screen.addstr(0,0,"Purged !")
            end_time = time.time()
            screen.addstr(0,0,text_presets.SCORE_BOARD(score,score+1,round(end_time - start_time,2)))
            screen.getch()
            break



def conquer_hell(screen,hell_n):
    with open(f"CirclesOfRegEx/{hell_n}.json","r") as out:
        hell = json.load(out)
    score = 0
    start_time = time.time()
    for challange in hell:  
        after_x_lines_render = challange['match'].count('\n')+1
        screen.addstr(0,0,challange["description"])
        screen.addstr(1,0,challange["match"])
        screen.addstr(after_x_lines_render,0,"\n")
        screen.addstr(after_x_lines_render+1,0,"Type your regex!\n")
        usr_in = utils.get_user_in(screen)
        screen.clear()
        if utils.test(usr_in,challange["match"],challange["result"]): 
            screen.addstr(0,0,"Conquered !")
            score+=1
        else:
            screen.addstr(0,0,"Purged !") 
        screen.refresh()
        time.sleep(0.5)
    end_time = time.time() 
    screen.addstr(0,0,text_presets.SCORE_BOARD(score,len(hell),round(end_time - start_time,2)))
    screen.refresh()
    screen.getch()



def main(stdscr):
    intro(stdscr)
    while True:
        selected_hell = hell_selection(stdscr)
        if not selected_hell:
            break
        infinite_hell(stdscr) if selected_hell == "9" else conquer_hell(stdscr,selected_hell)


curses.wrapper(main)
