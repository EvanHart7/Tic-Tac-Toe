import random


a = ' '
b = ' '
c = ' '
d = ' '
e = ' '
f = ' '
g = ' '
h = ' '
i = ' '
playing = True
outcome = ''
count = 0
moveOne = ''
moveTwo = ''
moveThree = ''


def Move3():
    
    global count
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global firstMove
    global secondMove
    global thirdMove
    
    if (firstMove == 'e'):
        if (secondMove == 'b'):
            if (thirdMove == 'c'):
                g = 'O'
            if (thirdMove == 'd'):
                f = 'O'
            if (thirdMove == 'f'):
                d = 'O'
            if (thirdMove == 'g'):
                c = 'O'
            if (thirdMove == 'i'):
                f = 'O'
        
        elif (secondMove == 'c'):
            if (thirdMove == 'd'):
                f = 'O'
            if (thirdMove == 'b'):
                d = 'O'
            if (thirdMove == 'f'):
                d = 'O'
            if (thirdMove == 'h'):
                d = 'O'
            if (thirdMove == 'i'):
                d = 'O'
        elif (secondMove == 'd'):
            f = 'O'
        elif (secondMove == 'f'):
            d = 'O'
        elif (secondMove == 'g'):
            c = 'O'
        elif (secondMove == 'h'):
            b = 'O'
        elif (secondMove == 'i'):
            c = 'O'

def Move2():
    
    global count
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global firstMove
    global secondMove
    global thirdMove
    
    if (firstMove == 'e'):
        if (secondMove == 'b'):
            h = 'O'
        elif (secondMove == 'c'):
            g = 'O'
        elif (secondMove == 'd'):
            f = 'O'
        elif (secondMove == 'f'):
            d = 'O'
        elif (secondMove == 'g'):
            c = 'O'
        elif (secondMove == 'h'):
            b = 'O'
        elif (secondMove == 'i'):
            c = 'O'



def Move1():
    
    global count
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    global firstMove
    global secondMove
    global thirdMove
    
    if (e == 'X'):
            a = 'O'
    else:
        e = "O"
     

def printResult():

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n')
    print('\n')
    print(outcome)
    print('\n')
    printBoard()
    print('\n')
    print('\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

def checkWin():
    
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    
    if (a == 'X' and b == 'X' and c == 'X') or (d == 'X' and e == 'X' and f == 'X') or (g == 'X' and h == 'X' and i == 'X'):
        return '1'
    if (a == 'O' and b == 'O' and c == 'O') or (d == 'O' and e == 'O' and f == 'O') or (g == 'O' and h == 'O' and i == 'O'):
        return '2'
    if (a == 'X' and d == 'X' and g == 'X') or (b == 'X' and e == 'X' and h == 'X') or (c == 'X' and f == 'X' and i == 'X'):
        return '1'
    if (a == 'O' and d == 'O' and g == 'O') or (b == 'O' and e == 'O' and h == 'O') or (c == 'O' and f == 'O' and i == 'O'):
        return '2'
    if (a == 'X' and e == 'X' and i == 'X') or (g == 'X' and e == 'X' and c == 'X'):
        return '1'
    if (a == 'O' and e == 'O' and i == 'O') or (g == 'O' and e == 'O' and c == 'O'):
        return '2'
    

def printBoard():
    print(' ' + a + ' | ' + b + ' | ' + c + ' ')
    print('-----------')
    print(' ' + d + ' | ' + e + ' | ' + f + ' ')
    print('-----------')
    print(' ' + g + ' | ' + h + ' | ' + i + ' ')

def playHardCom():
    global playing
    while playing:
    
        printBoard()
        
        global count
        global a
        global b
        global c
        global d
        global e
        global f
        global g
        global h
        global i
        global outcome
        global firstMove
        global secondMove
        global thirdMove
        
        badMove = True
        while badMove:
            print('Player 1 move')
            move = input("(TL, TM, TR, ML, MM, MR, BL, BM, BR)")
    

            if move == 'TL':
                if a == ' ':
                    a = 'X'
                    badMove = False
                    if count == 0:
                        firstMove = 'a'
                    elif count == 2:
                        secondMove = 'a'
                    elif count == 4:
                        thirdMove = 'a'
                    
                else:
                    print('Spot Already Taken')
                
            elif move == 'TM':
                if b == ' ':
                    b = 'X'
                    badMove = False
                    if count == 0:
                        firstMove = 'b'
                    elif count == 2:
                        secondMove = 'b'
                    elif count == 4:
                        thirdMove = 'b'
                else:
                    print('Spot Already Taken')
            elif move == 'TR':
                if c == ' ':
                    c = 'X'
                    badMove = False
                    if count == 0:
                        firstMove = 'c'
                    elif count == 2:
                        secondMove = 'c'
                    elif count == 4:
                        thirdMove = 'c'
                else:
                    print('Spot Already Taken')
            elif move == 'ML':
                if d == ' ':
                    d = 'X'
                    badMove = False
                    if count == 0:
                        firstMove = 'd'
                    elif count == 2:
                        secondMove = 'd'
                    elif count == 4:
                        thirdMove = 'd'
                else:
                    print('Spot Already Taken')
            elif move == 'MM':
                if e == ' ':
                    e = 'X'
                    badMove = False
                    if count == 0:
                        firstMove = 'e'
                    elif count == 2:
                        secondMove = 'e'
                    elif count == 4:
                        thirdMove = 'e'
                else:
                    print('Spot Already Taken')
            elif move == 'MR':
                if f == ' ':
                    f = 'X'
                    badMove = False
                    if count == 0:
                        firstMove = 'f'
                    elif count == 2:
                        secondMove = 'f'
                    elif count == 4:
                        thirdMove = 'f'
                else:
                    print('Spot Already Taken')
            elif move == 'BL':
                if g == ' ':
                    g = 'X'
                    badMove = False
                    if count == 0:
                        firstMove = 'g'
                    elif count == 2:
                        secondMove = 'g'
                    elif count == 4:
                        thirdMove = 'g'
                else:
                    print('Spot Already Taken')
            elif move == 'BM':
                if h == ' ':
                    h = 'X'
                    badMove = False
                    if count == 0:
                        firstMove = 'h'
                    elif count == 2:
                        secondMove = 'h'
                    elif count == 4:
                        thirdMove = 'h'
                else:
                    print('Spot Already Taken')
            elif move == 'BR':
                if i == ' ':
                    i = 'X'
                    badMove = False
                    if count == 0:
                        firstMove = 'i'
                    elif count == 2:
                        secondMove = 'i'
                    elif count == 4:
                        thirdMove = 'i'
                else:
                    print('Spot Already Taken')
            else:
                print('Invalid Move')
            
        count = count + 1
            
        if checkWin() == '1':
            outcome = 'Player 1 is the Winner!'
            break
        
        if count == 9:
            outcome = 'It is a tie!'
            break
            
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        
        
        badMove = True
        if count == 1:
            Move1()
        
        if count == 3:
            Move2()
        
        if count == 5:
            Move3()
        
        if count == 7:
            Move4()
        
        count = count + 1
        
        if checkWin() == '2':
            outcome = 'The Computer is the Winner!'
            break


def playEasyCom():
    global playing
    while playing:
    
        printBoard()
        
        global count
        global a
        global b
        global c
        global d
        global e
        global f
        global g
        global h
        global i
        global outcome
        
        badMove = True
        while badMove:
            print('Player 1 move')
            move = input("(TL, TM, TR, ML, MM, MR, BL, BM, BR)")
    

            if move == 'TL':
                if a == ' ':
                    a = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
                
            elif move == 'TM':
                if b == ' ':
                    b = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'TR':
                if c == ' ':
                    c = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'ML':
                if d == ' ':
                    d = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'MM':
                if e == ' ':
                    e = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'MR':
                if f == ' ':
                    f = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'BL':
                if g == ' ':
                    g = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'BM':
                if h == ' ':
                    h = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'BR':
                if i == ' ':
                    i = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            else:
                print('Invalid Move')
            
        count = count + 1
            
        if checkWin() == '1':
            outcome = 'Player 1 is the Winner!'
            break
        
        if count == 9:
            outcome = 'It is a tie!'
            break
            
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        
        
        badMove = True
        while badMove:
            rand = random.randint(1, 9)
            if (rand == 1 and a == ' '):
                a = 'O'
                badMove = False
            elif (rand == 2 and b == ' '):
                b = 'O'
                badMove = False
            elif (rand == 3 and c == ' '):
                c = 'O'
                badMove = False
            elif (rand == 4 and d == ' '):
                d = 'O'
                badMove = False
            elif (rand == 5 and e == ' '):
                e = 'O'
                badMove = False
            elif (rand == 6 and f == ' '):
                f = 'O'
                badMove = False
            elif (rand == 7 and g == ' '):
                g = 'O'
                badMove = False
            elif (rand == 8 and h == ' '):
                h = 'O'
                badMove = False
            elif (rand == 9 and i == ' '):
                i = 'O'
                badMove = False
        
        count = count + 1
        
        if checkWin() == '2':
            outcome = 'The Computer is the Winner!'
            break
            



def playHuman():
    
    global playing
    while playing:
    
        printBoard()
        
        global count
        global a
        global b
        global c
        global d
        global e
        global f
        global g
        global h
        global i
        global outcome
        
        badMove = True
        while badMove:
            print('Player 1 move')
            move = input("(TL, TM, TR, ML, MM, MR, BL, BM, BR)")
    

            if move == 'TL':
                if a == ' ':
                    a = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
                
            elif move == 'TM':
                if b == ' ':
                    b = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'TR':
                if c == ' ':
                    c = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'ML':
                if d == ' ':
                    d = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'MM':
                if e == ' ':
                    e = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'MR':
                if f == ' ':
                    f = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'BL':
                if g == ' ':
                    g = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'BM':
                if h == ' ':
                    h = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'BR':
                if i == ' ':
                    i = 'X'
                    badMove = False
                else:
                    print('Spot Already Taken')
            else:
                print('Invalid Move')
            
        count = count + 1
            
        if checkWin() == '1':
            outcome = 'Player 1 is the Winner!'
            break
        
        if count == 9:
            outcome = 'It is a tie!'
            break
            
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
        printBoard()
        
        
        badMove = True
        while badMove:
            print('Player 1 move')
            move = input("(TL, TM, TR, ML, MM, MR, BL, BM, BR)")
    

            if move == 'TL':
                if a == ' ':
                    a = 'O'
                    badMove = False
                else:
                    print('Spot Already Taken')
                
            elif move == 'TM':
                if b == ' ':
                    b = 'O'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'TR':
                if c == ' ':
                    c = 'O'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'ML':
                if d == ' ':
                    d = 'O'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'MM':
                if e == ' ':
                    e = 'O'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'MR':
                if f == ' ':
                    f = 'O'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'BL':
                if g == ' ':
                    g = 'O'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'BM':
                if h == ' ':
                    h = 'O'
                    badMove = False
                else:
                    print('Spot Already Taken')
            elif move == 'BR':
                if i == ' ':
                    i = 'O'
                    badMove = False
                else:
                    print('Spot Already Taken')
            else:
                print('Invalid Move')
        
        count = count + 1
        
        if checkWin() == '2':
            outcome = 'Player 2 is the Winner!'
            break
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        

print('Welcome to Tic Tac Toe!') 
print('\n')
print("Which Game Would You Like To Play? ")
game = input("Human (H) - Easy Computer (E) - Impossible Computer (I)")

if game == 'H':
    playHuman()
elif game == 'E':
    playEasyCom()
elif game == 'I':
    playHardCom()
    
printResult()
