from tkinter import *
import random

def next_turn(row=None, col=None):
    global player

    if row is not None and col is not None:
        if buttons[row][col]['text'] == "" and check_winner() is False:
            buttons[row][col]['text'] = player
            buttons[row][col].config(fg='blue' if player == 'x' else 'red')

            if check_winner() is False:
                player = players[1] if player == players[0] else players[0]
                label.config(text=(player + " turn"))
                if player == ai_player:
                    ai_move()
            elif check_winner() is True:
                label.config(text=(player + " wins!"))
            elif check_winner() == "Tie":
                label.config(text=("Tie!"))
    elif player == ai_player:
        ai_move()

def ai_move():
    empty_cells = [(r, c) for r in range(3) for c in range(3) if buttons[r][c]['text'] == ""]
    if empty_cells:
        row, col = random.choice(empty_cells)
        next_turn(row, col)

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            buttons[0][col].config(bg="green")
            buttons[1][col].config(bg="green")
            buttons[2][col].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    if empty_spaces() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg="yellow")
        return "Tie"

    return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] != "":
                spaces -= 1
    return spaces != 0

def new_game():
    global player, ai_player
    player = random.choice(players)
    ai_player = players[1] if player == players[0] else players[0]
    label.config(text=player + " turn")
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="", bg="#F0F0F0")
    if player == ai_player:
        ai_move()

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)
ai_player = players[1] if player == players[0] else players[0]
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                   command=lambda row=row, col=col: next_turn(row, col))
        buttons[row][col].grid(row=row, column=col)

if player == ai_player:
    ai_move()

window.mainloop()
