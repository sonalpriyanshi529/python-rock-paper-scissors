# from playsound import playsound
from tkinter import *
import random

win = Tk()
win.title('Stone Paper Scissor Game')
win.geometry('530x500')

scores = 0
comp_scores = 0

value = ['👊', '📄', '✂']

# comp = random.choice(value)

Label(text='', font=('Arial bold', 100)).grid(column=0, row=1, ipadx=80)
Label(text='', font=('Arial bold', 10)).grid(column=0, row=4)
Label(text='', font=('Arial bold', 60)).grid(column=0, row=5)
Label(text='').grid(column=0, row=9)


def exiting():
    top = Toplevel()
    top.geometry('350x150')
    top.title('Conclusion')

    top.resizable(0, 0)

    def ok():
        exit()

    if scores < comp_scores:
        Label(top, text='Comp Win', font=('Arial Bold', 50), bg='black', fg='white').grid(column=0, row=0)
        Label(top, text='', ).grid(column=0, row=1)
        Button(top, text='ok', padx=20, command=ok).grid(column=0, row=2)
        Label(top, text='sonal', font=('Arial Bold', 50), bg='black').grid(column=1, row=0)

    elif scores > comp_scores:
        Label(top, text='You Win', font=('Arial Bold', 50), bg='black', fg='white').grid(column=0, row=0)
        Label(top, text='', ).grid(column=0, row=1)
        Button(top, text='ok', padx=20, command=ok).grid(column=0, row=2)
        Label(top, text='sonal', font=('Arial Bold', 50), bg='black').grid(column=1, row=0)

    else:
        Label(top, text='Match Tie', font=('Arial Bold', 50), bg='black', fg='white').grid(column=0, row=0)
        Label(top, text='', ).grid(column=0, row=1)
        Button(top, text='ok', padx=20, command=ok).grid(column=0, row=2)
        Label(top, text='sonal', font=('Arial Bold', 50), bg='black').grid(column=1, row=0)


Button(text='Exit', padx=20, font=('Arial Bold', 10), command=exiting).grid(column=0, row=10, columnspan=3)

Label(text='Start the game', font=('Calisto MT', 40), bg='deeppink', fg='white', padx=90).grid(column=0, row=5,
                                                                                               columnspan=3)


def stone():
    global scores
    global comp_scores
    comp = random.choice(value)
    # playsound('zapsplat_multimedia_game_sound_water_drip_processed_single_002_58758.mp3')
    if comp == '👊':
        a = Label(text='👊', font=('Arial bold', 100), fg='red').grid(column=0, row=1)
        b = Label(text=comp, font=('Arial bold', 100), fg='blue').grid(column=2, row=1)
        c = Label(text='/', font=('Arial bold', 100)).grid(column=1, row=1)
        ans = Label(text='Match tie', font=('Calisto MT', 40), bg='deeppink', fg='white', padx=90).grid(column=0, row=5,
                                                                                                        columnspan=3)
        return a, b, c, ans

    if comp == '📄':
        a = Label(text='👊', font=('Arial bold', 100), fg='red').grid(column=0, row=1)
        b = Label(text=comp, font=('Arial bold', 100), fg='blue').grid(column=2, row=1)
        c = Label(text='/', font=('Arial bold', 100)).grid(column=1, row=1)
        ans = Label(text='Comp Win', font=('Calisto MT', 40), bg='deeppink', fg='white', padx=90).grid(column=0, row=5,
                                                                                                       columnspan=3)
        comp_scores = comp_scores + 10
        comp_sco = Label(text=f'Computer Score {comp_scores}', font=('Arial Bold', 10), padx=90, fg='blue').grid(
            column=0, row=8, columnspan=3)
        return a, b, c, ans, comp_sco

    if comp == '✂':
        a = Label(text='👊', font=('Arial bold', 100), fg='red').grid(column=0, row=1)
        b = Label(text=comp, font=('Arial bold', 90), fg='blue').grid(column=2, row=1)
        c = Label(text='/', font=('Arial bold', 100)).grid(column=1, row=1)
        ans = Label(text='You Win', font=('Calisto MT', 40), bg='deeppink', fg='white', padx=90).grid(column=0, row=5,
                                                                                                      columnspan=3)
        scores = scores + 10
        sco = Label(text=f'Your Score {scores}', font=('Arial Bold', 10), padx=90, fg='red').grid(column=0, row=7,
                                                                                                  columnspan=3)
        return a, b, c, ans, sco


Button(text='👊', font=('Arial bold', 40), command=stone, border=5, relief=GROOVE).grid(column=0, row=2)


def paper():
    global scores
    global comp_scores
    comp = random.choice(value)
    # playsound('G:\sonal coding\PYTHON
    # PROJECTS\GUI\Projects\zapsplat_multimedia_game_sound_water_drip_processed_single_002_58758.mp3')
    if comp == '👊':
        a = Label(text='📄', font=('Arial bold', 100), fg='red').grid(column=0, row=1)
        b = Label(text=comp, font=('Arial bold', 100), fg='blue').grid(column=2, row=1)
        c = Label(text='/', font=('Arial bold', 100)).grid(column=1, row=1)
        ans = Label(text='You Win', font=('Calisto MT', 40), bg='deeppink', fg='white', padx=90).grid(column=0, row=5,
                                                                                                      columnspan=3)
        scores = scores + 10
        sco = Label(text=f'Your Score {scores}', font=('Arial Bold', 10), padx=90, fg='red').grid(column=0, row=7,
                                                                                                  columnspan=3)
        return a, b, c, ans, sco

    if comp == '📄':
        a = Label(text='📄', font=('Arial bold', 100), fg='red').grid(column=0, row=1)
        b = Label(text=comp, font=('Arial bold', 100), fg='blue').grid(column=2, row=1)
        c = Label(text='/', font=('Arial bold', 100)).grid(column=1, row=1)
        ans = Label(text='Match Tie', font=('Calisto MT', 40), bg='deeppink', fg='white', padx=90).grid(column=0, row=5,
                                                                                                        columnspan=3)
        return a, b, c, ans

    if comp == '✂':
        a = Label(text='📄', font=('Arial bold', 100), fg='red').grid(column=0, row=1)
        b = Label(text=comp, font=('Arial bold', 90), fg='blue').grid(column=2, row=1)
        c = Label(text='/', font=('Arial bold', 100)).grid(column=1, row=1)
        ans = Label(text='Comp Win', font=('Calisto MT', 40), bg='deeppink', fg='white', padx=90).grid(column=0, row=5,
                                                                                                       columnspan=3)
        comp_scores = comp_scores + 10
        comp_sco = Label(text=f'Computer Score {comp_scores}', font=('Arial Bold', 10), padx=90, fg='blue').grid(
            column=0, row=8, columnspan=3)
        return a, b, c, ans, comp_sco


Button(text='📄', font=('Arial bold', 40), command=paper, border=5, relief=GROOVE).grid(column=1, row=2, sticky=W)


def scissor():
    global scores
    global comp_scores
    comp = random.choice(value)
    # playsound('G:\sonal coding\PYTHON
    # PROJECTS\GUI\Projects\zapsplat_multimedia_game_sound_water_drip_processed_single_002_58758.mp3')
    if comp == '👊':
        a = Label(text='✂', font=('Arial bold', 100), fg='red').grid(column=0, row=1)
        b = Label(text=comp, font=('Arial bold', 100), fg='blue').grid(column=2, row=1)
        c = Label(text='/', font=('Arial bold', 100)).grid(column=1, row=1)
        ans = Label(text='Comp Win', font=('Calisto MT', 40), bg='deeppink', fg='white', padx=90).grid(column=0, row=5,
                                                                                                       columnspan=3)
        comp_scores = comp_scores + 10
        comp_sco = Label(text=f'Computer Score {comp_scores}', font=('Arial Bold', 10), padx=90, fg='blue').grid(
            column=0, row=8, columnspan=3)
        return a, b, c, ans, comp_sco

    if comp == '📄':
        a = Label(text='✂', font=('Arial bold', 100), fg='red').grid(column=0, row=1)
        b = Label(text=comp, font=('Arial bold', 100), fg='blue').grid(column=2, row=1)
        c = Label(text='/', font=('Arial bold', 100)).grid(column=1, row=1)
        ans = Label(text='You Win', font=('Calisto MT', 40), bg='deeppink', fg='white', padx=90).grid(column=0, row=5,
                                                                                                      columnspan=3)
        scores = scores + 10
        sco = Label(text=f'Your Score {scores}', font=('Arial Bold', 10), padx=90, fg='red').grid(column=0, row=7,
                                                                                                  columnspan=3)
        return a, b, c, ans, sco

    if comp == '✂':
        a = Label(text='✂', font=('Arial bold', 100), fg='red').grid(column=0, row=1)
        b = Label(text=comp, font=('Arial bold', 90), fg='blue').grid(column=2, row=1)
        c = Label(text='/', font=('Arial bold', 100)).grid(column=1, row=1)
        ans = Label(text='Match Tie', font=('Calisto MT', 40), bg='deeppink', fg='white', padx=90).grid(column=0, row=5,
                                                                                                        columnspan=3)
        return a, b, c, ans


Button(text='✂', font=('Arial bold', 40), command=scissor, border=5, relief=GROOVE).grid(column=2, row=2, sticky=W,
                                                                                         padx=30)

win.mainloop()
