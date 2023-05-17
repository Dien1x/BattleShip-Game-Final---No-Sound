from Functions import *


PRINT_SHIPS = False


window = Tk()
window.title("Ναυμαχία The D-Game")
image = PhotoImage(file="Battleship_icon.png")
window.iconphoto(True, image)
window.resizable(False, False)
window.protocol("WM_DELETE_WINDOW", lambda: True)
font = PhotoImage(file="icons\\font.png")
background = Label(window, image=font, name="background")
background.place(x=0, y=0)

# Δημιουργία οντοτήτων για χρήση πλοιων
friend = Ship()
enemy = Ship()

## Icons
# Sea
sea_image = PhotoImage(file="icons\\sea.png")
sea_image_label = PhotoImage(file="icons\\sea_label.png")
sea_image_big = PhotoImage(file="icons\\sea_big.png")

# Buttons
red_image_big = PhotoImage(file="icons\\red_big.png")
white_image_big = PhotoImage(file="icons\\white_big.png")
grey_image_big = PhotoImage(file="icons\\grey_big.png")

# Labels
red_image_label = PhotoImage(file="icons\\red_label.png")
white_image_label = PhotoImage(file="icons\\white_label.png")
grey_image_label = PhotoImage(file="icons\\grey_label.png")

# Arrows
down_arrow = PhotoImage(file="icons\\arrow_down.png")
right_arrow = PhotoImage(file="icons\\arrow_right.png")
up_arrow = PhotoImage(file="icons\\arrow_up.png")
left_arrow = PhotoImage(file="icons\\arrow_left.png")

# Ships
aircraft_carrier_image = PhotoImage(file="icons\\aircraft_carrier.png")
battleship_image = PhotoImage(file="icons\\battleship.png")
cruiser_image = PhotoImage(file="icons\\cruiser.png")
destroyer_image = PhotoImage(file="icons\\destroyer.png")

# Difficulty
easy_icon = PhotoImage(file="icons\\easy.png")
hard_icon = PhotoImage(file="icons\\hard.png")


# All widgets for the game
# Ετικέτα που εμφανίζει στο παράθυρο το όνομα παίχτη
active_player = Label(window,
                      text=f"Όνομα Παίχτη",
                      font=("Comic Sans MS", 20),
                      name="active_player")

# Ετικέτα που εμφανίζει στο παράθυρο το Score
score = Label(window,
              text="Όνομα Παίχτη: 0\tCPU: 0",
              font=("Comic Sans MS", 15),
              name="score")

# Μία δομή για αποθήκευση όλων των ετικετών που απαρτίζουν το Ταμπλό του Παίχτη
frame_player = Frame(window, highlightthickness=5, name="frame_player")

# Μία δομή για αποθήκευση όλων των κουμπιών που απαρτίζουν το Ταμπλό του Εχθρού
frame_enemy = Frame(window, highlightthickness=5, name="frame_enemy")

# Μία δομή για αποθήκευση των κουμπιών για τοποθέτηση πλοίων
frame_ship_input = Frame(window, padx=15, pady=15, name="frame_ship_input")

# Μία δομή για αποθήκευση των κουμπιών "Νέο Παιχνίδι" και "Έξοδος"
frame_start_stop = Frame(window, name="end_frame")

# Τοποθέτηση κουμπιών στη δομή start_stop
# Κουμπί για πιθανή έναρξη νέου παιχνιδιού
Button(frame_start_stop, text="Νέο Παιχνίδι",
       font=("Comic Sans MS", 15), command=lambda: new_game(window, player_name_win, end_game_win, friend, enemy, sea_image, sea_image_label)).grid(row=0, column=0, padx=15)
# Κουμπί για πιθανή έξοδος απο το Παιχνίδι
Button(frame_start_stop, text="Έξοδος",
       font=("Comic Sans MS", 15), command=lambda: window.destroy()).grid(row=0, column=1, padx=15)

# Τοποθέτηση κουμπιών στη δομή ship_input
# Κουμπί για προσθήκη Πλοίου
ship_add = Button(frame_ship_input, text="Πρόσθεσε Πλοίο", command=lambda: create_ship_button(choose_ship_win, friend),
                  font=("Comic Sans MS", 15),
                  name="ship_add")
# Κουμπί για αφαίρεση Πλοίου
ship_remove = Button(frame_ship_input, text="Διέγραψε Πλοίο", command=lambda: remove_ship(remove_ship_win, friend),
                     font=("Comic Sans MS", 15), state=DISABLED,
                     name="ship_remove")
# Κουμπί για Έναρξη Παιχνιδιού
start = Button(frame_ship_input, text="Έναρξη παιχνιδιού",
               font=("Comic Sans MS", 15),
               command=lambda: start_game(window,
                                          enemy,
                                          friend,
                                          end_game_win,
                                          red_image_label,
                                          white_image_label,
                                          grey_image_label,
                                          red_image_big,
                                          white_image_big,
                                          sea_image,
                                          PRINT_SHIPS),
               state=DISABLED,
               name="start")
start.grid(row=1, column=0, columnspan=2, padx=10)
ship_add.grid(row=0, column=0, padx=10)
ship_remove.grid(row=0, column=1, padx=10)

# Τοποθέτηση κουμπιών στη δομή frame_enemy
# Δημιουργία και εισαγωγή των κουμπιών στο ταμπλό του εχθρού
for x in range(10):
    for y in range(11):
        Button(frame_enemy, text=f"{x+1}, {y+1}",
               command="", image=sea_image,
               name=f"enemy{x}{y}",).grid(row=x, column=y)
        
# Δημιουργία και εισαγωγή των ετικετών στο ταμπλό του Παίχτη
for x in range(10):
    for y in range(11):
        Label(frame_player, text=f"{x+1}, {y+1}",
              image=sea_image_label,
              name=f"player{x}{y}").grid(row=x, column=y)


# Στοίχιση δομών στο παράθυρο
frame_player.grid(row=3, column=1, columnspan=2)
frame_enemy.grid(row=0, column=0, rowspan=5)
frame_ship_input.grid(row=6, column=0, rowspan=2, columnspan=5)
frame_start_stop.grid(row=4, column=1, columnspan=2)
active_player.grid(row=0, column=1, columnspan=2)
score.grid(row=1, column=1, columnspan=2)


#########################################################################################


# player_name window
player_name_win = Toplevel(window)
player_name_win.protocol("WM_DELETE_WINDOW", lambda: True)
player_name_win.resizable(False, False)

# All widgets for the give player Name
frame_player_name = Frame(player_name_win, name = "frame_player_name")
player_name_win.withdraw()


def player_name():
    """
    Συνάρτηση Ονομασίας Παίχτη.

    Η συνάρτηση αυτή αρχικοποιει το όνομα του παιχτη και ξεκινάει το παιχνίδι.
    """
    Ship.ACTIVE_PLAYER_NAME = player_name_win.nametowidget(f"frame_player_name.player_name_box").get()
    window.nametowidget("active_player").config(text=Ship.ACTIVE_PLAYER_NAME)
    window.nametowidget("score").config(text=f"{Ship.ACTIVE_PLAYER_NAME}: 0\tCPU: 0")
    

    player_name_win.withdraw()
    player_name_win.grab_release()


Label(frame_player_name,
      text="Παρακαλώ δώστε το όνομά σας:",
      font=("Comic Sans MS", 20, "bold")).pack(pady=15)
Entry(frame_player_name, name="player_name_box",
      width=20,
      font=("Comic Sans MS", 20),
      justify=CENTER).pack()
Button(frame_player_name,
       text="Νέο Παιχνίδι",
       font=("Comic Sans MS", 14, "bold"),
       command=player_name).pack(pady=15)

# Προσθέτει τη δυνατότητα καταχώρησης ονόματος με το Enter
player_name_win.bind("<Return>", lambda event: player_name())

frame_player_name.pack()


#########################################################################################


# choose ship window
choose_ship_win = Toplevel(window)
choose_ship_win.protocol("WM_DELETE_WINDOW", lambda: True)
choose_ship_win.resizable(False, False)

# All widgets for the chose ship
frame_choose_ship = Frame(choose_ship_win, name = "frame_choose_ship")
choose_ship_win.withdraw()

# Κουμπί για δημιουργία πλοίου τύπου Aircraft Carrier.
aircraft_carrier_add = Button(frame_choose_ship, image=aircraft_carrier_image, name="aircraft_carrier_add",
                              command=lambda: choose_ship_length(window,
                                                                 choose_ship_win,
                                                                 choose_direction_win,
                                                                 friend,
                                                                 friend.AIRCRAFT_CARRIER)).pack(padx=20, pady=10)
# Κουμπί για δημιουργία πλοίου τύπου BattleShip.
battleship_add = Button(frame_choose_ship, image=battleship_image, name="battleship_add",
                        command=lambda: choose_ship_length(window,
                                                           choose_ship_win,
                                                           choose_direction_win,
                                                           friend,
                                                           friend.BATTLESHIP)).pack(padx=20, pady=10)
# Κουμπί για δημιουργία πλοίου τύπου Cruiser.
cruiser_add = Button(frame_choose_ship, image=cruiser_image, name="cruiser_add",
                     command=lambda: choose_ship_length(window,
                                                        choose_ship_win,
                                                        choose_direction_win,
                                                        friend,
                                                        friend.CRUISER)).pack(padx=20, pady=10)
# Κουμπί για δημιουργία πλοίου τύπου Destroyer.
destroyer_add = Button(frame_choose_ship, image=destroyer_image, name="destroyer_add",
                       command=lambda: choose_ship_length(window,
                                                          choose_ship_win,
                                                          choose_direction_win,
                                                          friend,
                                                          friend.DESTROYER)).pack(padx=20, pady=10)

frame_choose_ship.pack()
center_window(choose_ship_win)


#########################################################################################


# remove ship window
remove_ship_win = Toplevel(window)
remove_ship_win.protocol("WM_DELETE_WINDOW", lambda: True)
remove_ship_win.resizable(False, False)

# All widgets for the chose ship
frame_remove_ship = Frame(remove_ship_win, name = "frame_remove_ship")
remove_ship_win.withdraw()

# Κουμπί για δημιουργία πλοίου τύπου Aircraft Carrier.
aircraft_carrier_remove = Button(frame_remove_ship, image=aircraft_carrier_image, name="aircraft_carrier_remove",
                                 command=lambda: remove(window,
                                                        remove_ship_win,
                                                        friend,
                                                        friend.AIRCRAFT_CARRIER,
                                                        sea_image,
                                                        grey_image_big)).pack(padx=20, pady=10)
# Κουμπί για δημιουργία πλοίου τύπου BattleShip.
battleship_remove = Button(frame_remove_ship, image=battleship_image, name="battleship_remove",
                           command=lambda: remove(window,
                                                  remove_ship_win,
                                                  friend,
                                                  friend.BATTLESHIP,
                                                  sea_image,
                                                  grey_image_big)).pack(padx=20, pady=10)
# Κουμπί για δημιουργία πλοίου τύπου Cruiser.
cruiser_remove = Button(frame_remove_ship, image=cruiser_image, name="cruiser_remove",
                        command=lambda: remove(window,
                                               remove_ship_win,
                                               friend,
                                               friend.CRUISER,
                                               sea_image,
                                               grey_image_big)).pack(padx=20, pady=10)
# Κουμπί για δημιουργία πλοίου τύπου Destroyer.
destroyer_remove = Button(frame_remove_ship, image=destroyer_image, name="destroyer_remove",
                          command=lambda: remove(window,
                                                 remove_ship_win,
                                                 friend,
                                                 friend.DESTROYER,
                                                 sea_image,
                                                 grey_image_big)).pack(padx=20, pady=10)

frame_remove_ship.pack()
center_window(remove_ship_win)


#########################################################################################


# choose direction window
choose_direction_win = Toplevel(window)
choose_direction_win.protocol("WM_DELETE_WINDOW", lambda: True)
choose_direction_win.resizable(False, False)

# All widgets for the choose direction
arrows_frame = Frame(choose_direction_win, name = "arrows_frame")
choose_direction_win.withdraw()

# Κουμπιά για επιλογή κατεύθυνσης πλοίου
up = Button(arrows_frame, image=up_arrow,
            command=lambda: choose_ship_direction(window, choose_direction_win, friend, "up", grey_image_big), name="up")
down = Button(arrows_frame, image=down_arrow,
              command=lambda: choose_ship_direction(window, choose_direction_win, friend, "down", grey_image_big), name="down")
left = Button(arrows_frame, image=left_arrow,
              command=lambda: choose_ship_direction(window, choose_direction_win, friend, "left", grey_image_big), name="left")
right = Button(arrows_frame, image=right_arrow,
               command=lambda: choose_ship_direction(window, choose_direction_win, friend, "right", grey_image_big), name="right")
back = Button(arrows_frame, text="Back", font=("comic sans ms", 18, "bold"),
              command=lambda: cancel_direction(window, friend, choose_direction_win), name="back")

# Τοποθέτηση στου πλέγμα
up.grid(column=1, row=0)
down.grid(column=1, row=2)
left.grid(column=0, row=1)
right.grid(column=2, row=1)
back.grid(row=5, column=1, pady=10)

arrows_frame.pack()
center_window(choose_direction_win)

#########################################################################################


# end game window
end_game_win = Toplevel(window)
end_game_win.protocol("WM_DELETE_WINDOW", lambda: True)
end_game_win.resizable(False, False)

# All widgets for the end game
end_game_frame = Frame(end_game_win, name = "end_game_frame")
end_game_win.withdraw()

# Κουμπιά για επιλογή κατεύθυνσης πλοίου
end_game_label = Label(end_game_frame,
                       text = "O Παίχτης με το Όνομα: Όνομα, νίκησε!!!",
                       font=("Comic Sans MS", 20),
                       name="end_game_label").grid(row=0, column=1, pady=10)
# Κουμπί για πιθανή έναρξη νέου παιχνιδιού
end_new_game_button = Button(end_game_frame,
                             text="Νέο Παιχνίδι",
                             font=("Comic Sans MS", 15),
                             command=lambda: new_game(window, player_name_win, end_game_win, friend, enemy,sea_image, sea_image_label)).grid(row=1, column=0, padx=5)
# Κουμπί για πιθανή έξοδος απο το Παιχνίδι
end_exit_game_button = Button(end_game_frame,
                              text="Έξοδος",
                              font=("Comic Sans MS", 15),
                              command=lambda: window.destroy()).grid(row=1, column=2, padx=5)

end_game_frame.pack(padx=30, pady=30)
center_window(end_game_win)

#########################################################################################


center_window(window)
center_window(player_name_win)

player_name_win.deiconify()

player_name_win.lift()
player_name_win.grab_set()

window.mainloop()
