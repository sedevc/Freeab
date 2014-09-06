import curses

FILE_NAME_BOILER = 'bTemp.txt'
FILE_NAME_FIRE = 'fTemp.txt'
MIN_VALUE = 0
MAX_VALUE = 99

def wFile(stat, tempfile):
    file = open(tempfile, "w")
    file.write(str(stat))
    file.close()

def readSimTemp(x):
    f = open(x, 'r')
    return f.read()

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    stdscr.addstr(7, 0, "Boilder Temp: %d   Fire Temp: %d  " % (int(readSimTemp(FILE_NAME_BOILER)), int(readSimTemp(FILE_NAME_FIRE))))
    #print "Boilder Temp: %d   Fire Temp: %d  " % (int(readSimTemp(FILE_NAME_BOILER)), int(readSimTemp(FILE_NAME_FIRE)))
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP: 
        stdscr.addstr(2, 20, "B.TEMP +10C")
        wFile(int(readSimTemp(FILE_NAME_BOILER))+10, FILE_NAME_BOILER)
    elif key == curses.KEY_DOWN: 
        stdscr.addstr(3, 20, "B.TEMP -10C")
        wFile(int(readSimTemp(FILE_NAME_BOILER))-10, FILE_NAME_BOILER)
    elif key == curses.KEY_RIGHT: 
        stdscr.addstr(4, 20, "F.TEMP +20C")
        wFile(int(readSimTemp(FILE_NAME_FIRE))+20, FILE_NAME_FIRE)
    elif key == curses.KEY_LEFT: 
        stdscr.addstr(5, 20, "F.TEMP -20C")
        wFile(int(readSimTemp(FILE_NAME_FIRE))-20, FILE_NAME_FIRE)

curses.endwin()


