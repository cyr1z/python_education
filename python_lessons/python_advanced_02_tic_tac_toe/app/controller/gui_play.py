from functools import partial
from tkinter import filedialog, Tk, Frame, Text, Button


def quit_game(ev):
    global root
    root.destroy()


def load_log(ev):
    pass


def replay(ev):
    pass


def make_move(number):
    print(number)


root = Tk()
root.title('TicTacToe')
size = 186
panel_frame = Frame(root, height=60)
board_frame = Frame(root, height=100)
board_frame.config(width=size * 3, height=size * 3)
status_frame = Frame(root, height=60)

panel_frame.pack(side='top', fill='x')
status_frame.pack(side="top", fill='x')
board_frame.pack(side='bottom', fill='both', expand=1)
buttons = []
counter = 1

for i in range(0, 3):
    for j in range(0, 3):
        buttons.append(
            Button(
                board_frame,
                text=counter,
                command=partial(make_move, counter)
            )
        )
        buttons[counter - 1].place(
            x=size * j, y=size * i, width=size, height=size
        )
        counter += 1

new_game_button = Button(panel_frame, text='New Game')
new_robot_game_button = Button(panel_frame, text='New Game with Robot')
log_button = Button(panel_frame, text='View Game logs')
replay_button = Button(panel_frame, text='Replay')
quit_button = Button(panel_frame, text='Quit')

new_game_button.place(x=5, y=10, width=90, height=30)
new_robot_game_button.place(x=100, y=10, width=155, height=30)
log_button.place(x=260, y=10, width=115, height=30)
replay_button.place(x=380, y=10, width=80, height=30)
quit_button.place(x=465, y=10, width=80, height=30)

replay_button.bind("<Button-1>", replay)
quit_button.bind("<Button-1>", quit_game)

quit_button.bind("<Button-1>", quit_game)

if __name__ == "__main__":
    root.mainloop()
