from tkinter import Label, Tk, Button, Frame, messagebox
from PIL import ImageTk, Image
from random import choices

root = Tk()
root.title("TicToc")
endState = 0
player_win = 0
pcWin = 0
whoStart = 0


def start_again():
    global powList
    global endState
    global whoStart
    message = messagebox.askquestion(title=None, message='Do you wish to play again?')
    if message == 'yes':
        powList = [25, 25, 25, 25, 25, 25, 25, 25, 25]
        for k in range(9):
            buttonList[k].config(state='normal', image=emptyImg)
        endState = -1
        scoreLabel.config(text='                      \nplayer     pc   \n         ' + str(player_win) + '     :     '
                               + str(pcWin) + '         ')
        whoStart *= -1
        if whoStart == -1:
            pc_move()
    else:
        root.destroy()


def win_check():
    global endState
    global powList
    global player_win
    global pcWin
    endState = 0
    for k in range(3):
        if (powList[0+k]+powList[3+k]+powList[6+k] == -6 or powList[0+k*3]+powList[1+k*3]+powList[2+k*3] == -6
                or powList[0]+powList[4]+powList[8] == -6 or powList[2]+powList[4]+powList[6] == -6):
            endState = 1
        elif (powList[0+k]+powList[3+k]+powList[6+k] == -9 or powList[0+k*3]+powList[1+k*3]+powList[2+k*3] == -9
              or powList[0]+powList[4]+powList[8] == -9 or powList[2]+powList[4]+powList[6] == -9):
            endState = 3
        elif sum(powList) == -22 or sum(powList) == -23:
            endState = 2
    if endState == 1:
        player_win += 1
        scoreLabel.config(text='Congratulation you Win\nplayer     pc   \n         '
                               + str(player_win) + '     :     ' + str(pcWin) + '         ')
    elif endState == 2:
        scoreLabel.config(text='         Draw         \nplayer     pc   \n         ' + str(player_win) + '     :     '
                               + str(pcWin) + '         ')
    elif endState == 3:
        pcWin += 1
        scoreLabel.config(text='    Sorry you Loss    \nplayer     pc   \n         ' + str(player_win) + '     :     '
                               + str(pcWin) + '         ')
    if endState != 0:
        for button in buttonList:
            button.config(state='disabled')
        start_again()


def player_move(k):
    global endState
    if powList[k] > 0:
        if playerSign == 1:
            buttonList[k].config(image=circleImg)            
        else:
            buttonList[k].config(image=crossImg)
        powList[k] = -2
        win_check()
        if endState != -1:
            pc_move()
        win_check()


def pc_move():
    global endState
    for k in range(3):
        if powList[0+k]+powList[3+k]+powList[6+k] == 19:
            if powList[0+k] == -3 and powList[3+k] == -3:          powList[6+k] = 10000000
            if powList[0+k] == -3 and powList[6+k] == -3:          powList[3+k] = 10000000
            if powList[6+k] == -3 and powList[3+k] == -3:          powList[0+k] = 10000000
        elif powList[0+k*3]+powList[1+k*3]+powList[2+k*3] == 19:
            if powList[0+k*3] == -3 and powList[1+k*3] == -3:      powList[2+k*3] = 10000000
            if powList[1+k*3] == -3 and powList[2+k*3] == -3:      powList[0+k*3] = 10000000
            if powList[2+k*3] == -3 and powList[0+k*3] == -3:      powList[1+k*3] = 10000000
        elif powList[0]+powList[4]+powList[8] == 19:
            if powList[0] == -3 and powList[4] == -3:              powList[8] = 10000000
            if powList[4] == -3 and powList[8] == -3:              powList[0] = 10000000
            if powList[8] == -3 and powList[0] == -3:              powList[4] = 10000000
        elif powList[2]+powList[4]+powList[6] == 19:
            if powList[2] == -3 and powList[4] == -3:              powList[6] = 10000000
            if powList[4] == -3 and powList[6] == -3:              powList[2] = 10000000
            if powList[6] == -3 and powList[2] == -3:              powList[4] = 10000000
        if powList[0+k]+powList[3+k]+powList[6+k] == 21:
            if powList[0+k] == -2 and powList[3+k] == -2:          powList[6+k] = 10000
            if powList[3+k] == -2 and powList[6+k] == -2:          powList[0+k] = 10000
            if powList[6+k] == -2 and powList[0+k] == -2:          powList[3+k] = 10000
        elif powList[0+k*3]+powList[1+k*3]+powList[2+k*3] == 21:
            if powList[0+k*3] == -2 and powList[1+k*3] == -2:      powList[2+k*3] = 10000
            if powList[1+k*3] == -2 and powList[2+k*3] == -2:      powList[0+k*3] = 10000
            if powList[2+k*3] == -2 and powList[0+k*3] == -2:      powList[1+k*3] = 10000
        elif powList[0]+powList[4]+powList[8] == 21:
            if powList[0] == -2 and powList[4] == -2:              powList[8] = 10000
            if powList[4] == -2 and powList[8] == -2:              powList[0] = 10000
            if powList[8] == -2 and powList[0] == -2:              powList[4] = 10000
        elif powList[2]+powList[4]+powList[6] == 21:
            if powList[2] == -2 and powList[4] == -2:              powList[6] = 10000
            if powList[4] == -2 and powList[6] == -2:              powList[2] = 10000
            if powList[6] == -2 and powList[2] == -2:              powList[4] = 10000
    try:
        pc_choice = choices(buttonList, weights=powList, k=1)[0]
        powList[buttonList.index(pc_choice)] = -3
    except ValueError:
        return   
    if playerSign == 1:
        pc_choice.config(image=crossImg)
    else:
        pc_choice.config(image=circleImg)


# background load
bgdImg = ImageTk.PhotoImage(Image.open('Main Lable.png'))
mainLabel = Label(root, image=bgdImg)
mainLabel.grid(row = 0, column=0, columnspan=88, rowspan=110)
# score label
scoreLabel = Label(root, text=('                      \nplayer     pc   \n         ' + str(player_win) + '     :     ' + str(pcWin) + '         '))
scoreLabel.grid(row=14, column=29, columnspan=30, rowspan=16)
# help ruler
main_Ruler = Frame(root)
main_Ruler.grid(row=32, column=0, columnspan=10, rowspan=78)
# buttons
emptyImg = ImageTk.PhotoImage(Image.open('Empty.png'))
crossImg = ImageTk.PhotoImage(Image.open('Cross.png'))
circleImg = ImageTk.PhotoImage(Image.open('Circle.png'))
mainButton1 = Button(root, image=emptyImg, borderwidth=0, command=lambda: player_move(0))
mainButton2 = Button(root, image=emptyImg, borderwidth=0, command=lambda: player_move(1))
mainButton3 = Button(root, image=emptyImg, borderwidth=0, command=lambda: player_move(2))
mainButton4 = Button(root, image=emptyImg, borderwidth=0, command=lambda: player_move(3))
mainButton5 = Button(root, image=emptyImg, borderwidth=0, command=lambda: player_move(4))
mainButton6 = Button(root, image=emptyImg, borderwidth=0, command=lambda: player_move(5))
mainButton7 = Button(root, image=emptyImg, borderwidth=0, command=lambda: player_move(6))
mainButton8 = Button(root, image=emptyImg, borderwidth=0, command=lambda: player_move(7))
mainButton9 = Button(root, image=emptyImg, borderwidth=0, command=lambda: player_move(8))
buttonList = [mainButton1, mainButton2, mainButton3, mainButton4, mainButton5, mainButton6, mainButton7, mainButton8,
              mainButton9]
powList = [25, 25, 25, 25, 25, 25, 25, 25, 25]
mainButton1.grid(row = 34, column=10, columnspan=20, rowspan=20)
mainButton2.grid(row = 34, column=34, columnspan=20, rowspan=20)
mainButton3.grid(row = 34, column=58, columnspan=20, rowspan=20)
mainButton4.grid(row = 57, column=10, columnspan=20, rowspan=20)
mainButton5.grid(row = 57, column=34, columnspan=20, rowspan=20)
mainButton6.grid(row = 57, column=58, columnspan=20, rowspan=20)
mainButton7.grid(row = 80, column=10, columnspan=20, rowspan=20)
mainButton8.grid(row = 80, column=34, columnspan=20, rowspan=20)
mainButton9.grid(row = 80, column=58, columnspan=20, rowspan=20)
# starting ask message
message1 = messagebox.askquestion(title=None, message='Do you wish to start with o?')
message2 = messagebox.askquestion(title=None, message='Do you wish to be first player?')
# playerSign = 1 circle, playerSign = -1 cross
if message1 == 'yes':
    playerSign = 1
else:
    playerSign = -1
# whoStart = 1 player, whoStart = -1 pc
if message2 == 'yes':
    whoStart = 1
else:
    whoStart = -1
    pc_move()
root.mainloop()
