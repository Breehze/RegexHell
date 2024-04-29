HELLO = r'''______                       
| ___ \                      
| |_/ /___  __ _  _____  __
|    // _ \/ _` |/ _ \ \/ /
| |\ |  __| (_| |  __/>  < 
\_| \_\___|\__, |\___/_/\_\
            __/ |          
       _   ____/  _ _      
      | | | |    | | |     
      | |_| | ___| | |     
      |  _  |/ _ | | |     
      | | | |  __| | |     
      \_| |_/\___|_|_|     
                           
                                  
'''


MENU = '''     _  _       _  _ 
    | || | ___ | || |
    | __ |/ -_)| || |
    |_||_|\___||_||_|
  ---------------------
 | 1. Limbo            | Commandments: 
 | 2. This seems easy  | 1. Pick your Hell
 | 3. Still kinda easy | 2. Enter to start 
 | 4. Moderately easy  | 3. q to quit
 | 5. Ehhhhhhhhhhh     | 4. Conquer!
 | 6. Hmmmmmmmmmmmm    | 
 | 7. What the fuck    | 
 | 8. Clusterfuck      | 
 | 9. Brainfuck        | 
  ---------------------
'''

FIRST_HELL = '''

'''

SCORE_BOARD = lambda p_score,f_score,time : f'''
   ______________________________
 / \                             \.
|   |                            |.
 \_ |   Thine triumphs:          |.
    |                            |.
    |     {p_score}/{f_score} beaten!            |.''' + f"\n    |     Beaten in {time}"+ " "*(35 - len(f"    |     Beaten in {time}") -2)+"|." + '''
    |               seconds.     |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |                            |.
    |   _________________________|___
    |  /                            /.
    \_/____________________________/.
'''








