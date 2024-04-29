import curses
import re


def get_user_in(screen) -> str: 
    typed_in = [] 
    while True:
        screen.refresh()
        key = screen.getch()
        pos_y,pos_x = screen.getyx() 
        if key == 10:
            return ''.join(typed_in) 
        if key == curses.KEY_LEFT:
            screen.move(pos_y,pos_x-1) if pos_x != 0 else None
            continue
        if key == curses.KEY_RIGHT:
            screen.move(pos_y,pos_x+1) if pos_x != len(typed_in) else None
            continue
        if key == curses.KEY_BACKSPACE:
            if pos_x - 1 != -1:
                typed_in.pop(pos_x-1) 
        else:
            typed_in.append(chr(key))
        screen.move(pos_y,0)
        screen.clrtoeol()
        screen.addstr(pos_y,0,''.join(typed_in))

def test(usr_in,string,wntd) -> bool:
    try:
        assert re.findall(rf"{usr_in.strip()}",string, flags=re.MULTILINE) == wntd
        return True
    except AssertionError:
        return False


